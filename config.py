import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev_secret_key') # Aller dans le Docker
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', 'mysql+pymysql://root:secret@db:3306/users') 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'informations-sur-les-utilisateurs')
    JWT_EXPIRATION_SECONDS = 7200  # 2 heures

