import jwt
from datetime import datetime, timedelta
from config import Config
from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(password):
    return generate_password_hash(password)

def verify_password(password, hashed_password):
    return check_password_hash(hashed_password, password)

def generate_jwt(user):
    payload = {
        'pseudo': user.pseudo,
        'exp': datetime.utcnow() + timedelta(seconds=Config.JWT_EXPIRATION_SECONDS)
    }
    token = jwt.encode(payload, Config.JWT_SECRET_KEY, algorithm='HS256')
    return token
