from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    email = db.Column(db.String(120), primary_key=True)
    pseudo = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(512), nullable=False)

    # Champs nécessaires pour /whois, /seen, /ison :
    roles = db.Column(db.String(120), default='user')     # ex: 'user,admin'
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)  # datetime de la dernière activité
    channels = db.Column(db.String(200), default='')       # ex: "#general,#random"

    def to_public_dict(self):
        return {
            "pseudo": self.pseudo,
            "roles": self.roles.split(",") if self.roles else [],
            "channels": self.channels.split(",") if self.channels else []
        }

