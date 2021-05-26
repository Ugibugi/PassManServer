from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Vault(db.Model):
    __tablename__ = 'vaults'
    id = db.Column(db.Integer, primary_key = True)
    pubk = db.Column(db.String())
    name = db.Column(db.String())
    passwords = db.relationship('Password', backref = "vault")

    def __init__(self, pubk, name):
        self.pubk = pubk
        self.name = name

class Password(db.Model):
    __tablename__ = 'passwords'
    id = db.Column(db.Integer, primary_key = True)
    vault_id = db.Column(db.Integer, db.ForeignKey('vaults.id'))
    name = db.Column(db.String())
    value = db.Column(db.String())
    
    def __init__(self, name, value, vault_id):
        self.vault_id = vault_id
        self.name = name
        self.value = value



