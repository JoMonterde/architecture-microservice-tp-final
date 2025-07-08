import jwt
import datetime
from flask import Flask, request, jsonify
from user import db, User
from auth import hash_password, generate_jwt, verify_password
from config import Config
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)
app.config["SQLALCHEMY_DATABASE_URI"] = (Config.SQLALCHEMY_DATABASE_URI)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
with app.app_context():
    db.create_all()

@app.route("/register", methods=["POST"])
def register():
    """
    Création de compte utilisateur
    ---
    post:
      summary: Création de compte utilisateur
      description: Permet de créer un nouveau compte utilisateur à partir d’un pseudo, d’un mot de passe et d’un email.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - pseudo
                - email
                - password
              properties:
                pseudo:
                  type: string
                  example: Morgane
                email:
                  type: string
                  format: email
                  example: morgane@gmail.com
                password:
                  type: string
                  format: password
                  example: H4iWy
      responses:
        201:
          description: Le compte a été créé avec succès
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                    example: ok
                  reponse:
                    type: string
                    example: Compte créé
        400:
          description: Données manquantes dans la requête
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                    example: ko
                  reponse:
                    type: string
                    example: Erreur : pseudo et/ou email et/ou password manquant(s)
        409:
          description: Conflit - utilisateur déjà existant
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                    example: ko
                  reponse:
                    type: string
                    example: Erreur : l'adresse e-mail morgane@gmail.com est déjà utilisée.
    """
    data = request.get_json()
    pseudo = data.get("pseudo")
    email = data.get("email")
    password = data.get("password")
    if not pseudo or not email or not password:
        return jsonify({"error": "pseudo et/ou email et/ou password manquant(s)"}), 400
    
    if User.query.filter((User.pseudo == pseudo) | (User.email == email)).first():
        return jsonify({'error': 'User already exists'}), 409

    new_user = User(
        pseudo=pseudo,
        email=email,
        password_hash=hash_password(password)
    )

    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "Compte créé"}), 201

@app.route('/login', methods=['POST'])
def login():
"""
    Connexion utilisateur
    ---
    post:
      summary: Connexion utilisateur
      description: Authentifie un utilisateur à partir de son email et mot de passe, et retourne un token JWT si les identifiants sont valides.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - email
                - password
              properties:
                email:
                  type: string
                  format: email
                  example: morgane@gmail.com
                password:
                  type: string
                  format: password
                  example: H4iWy
      responses:
        200:
          description: Authentification réussie
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                    example: ok
                  reponse:
                    type: object
                    properties:
                      token:
                        type: string
                        example: eyJ0eXAiOiJKV1QiLCJhbGci...
        401:
          description: Identifiants invalides
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                    example: ko
                  reponse:
                    type: string
                    example: Erreur : email et/ou mot de passe invalide(s)
    """
    data = request.get_json()
    pseudo = data.get('pseudo')
    password = data.get('password')

    if not pseudo or not password:
        return jsonify({
            "status": "ko",
            "reponse": "Pseudo et mot de passe requis"
        }), 400

    user = User.query.filter_by(pseudo=pseudo).first()

    if not user or not verify_password(password, user.password_hash):
        return jsonify({
            "status": "ko",
            "reponse": "Pseudo et/ou mot de passe invalide(s)"
        }), 401

    # Génération du token
    token = generate_jwt(user)
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(seconds=Config.JWT_EXPIRATION_SECONDS)

    # Stocker le token et son expiration dans la base
    user.current_token = token
    user.token_expiration = expiration_time
    user.last_seen = datetime.datetime.utcnow()

    db.session.commit()

    return jsonify({
        "status": "ok",
        "reponse": {
            "token": token
        }
    }), 200

@app.route("/whois/<pseudo>", methods=["GET"])
def whois(pseudo):
    user = User.query.filter_by(pseudo=pseudo).first()
    if not user:
        return jsonify({
            "status": "ko",
            "reponse": "Utilisateur introuvable"
        }), 404
    return jsonify({
        "status": "ok",
        "reponse": user.to_public_dict()
    }), 200


@app.route("/ison", methods=["GET"])
def ison():
    users_param = request.args.get("users")
    if not users_param:
        return jsonify({
            "status": "ko",
            "reponse": "Paramètre 'users' manquant"
        }), 400

    online = []
    # Format attendu : "pseudo1:token1,pseudo2:token2"
    user_tokens = users_param.split(",")
    for ut in user_tokens:
        try:
            pseudo, token = ut.split(":")
        except ValueError:
            continue

        try:
            payload = jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=["HS256"])
            if payload.get("pseudo") == pseudo:
                online.append(pseudo)
        except jwt.ExpiredSignatureError:
            continue
        except jwt.InvalidTokenError:
            continue

    return jsonify({
        "status": "ok",
        "reponse": {
            "online_users": online
        }
    }), 200


@app.route("/protected")
def protected():
    auth = request.headers.get("Authorization", "")
    if not auth.startswith("Bearer "):
        return jsonify({"error": "Token manquant"}), 401
    
    token = auth[7:]
    try:
        decoded = jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=["HS256"])
        return jsonify({"status": "ok", "user": decoded["pseudo"]})
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token expiré"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Token invalide"}), 401



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

