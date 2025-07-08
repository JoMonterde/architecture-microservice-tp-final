import jwt
import datetime
from flask import Flask, request, jsonify
from user import db, User
from auth import hash_password, generate_jwt
from config import Config

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (Config.SQLALCHEMY_DATABASE_URI)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
with app.app_context():
    db.create_all()

@app.route("/afficher", methods=["GET"])
def afficher():
    return "test aff"

@app.route("/register", methods=["POST"])
def register():
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
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(pseudo=pseudo).first()
    if not user or not hash_password(password) == user.password_hash:
        return jsonify({'error': 'Pseudo et/ou mot de passe invalide(s)'}), 401

    token = generate_jwt(user)
    return jsonify({'token': token}), 200

@app.route("/protected")
def protected():
    auth = request.headers.get("Authorization", "")
    if not auth.startswith("Bearer "):
        return jsonify({"error": "Token manquant"}), 401

    token = auth[7:]
    try:
        decoded = jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=["HS256"])
        return jsonify({"status": "ok", "user": decoded["user"]})
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token expiré"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Token invalide"}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
