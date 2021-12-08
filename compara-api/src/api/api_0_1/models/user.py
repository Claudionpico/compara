from model import *


class User(Model, db.Model):
    __tablename__ = 'user'

    dni = db.Column(db.String(50))
    client_cuit = db.Column(db.String(255))
    name = db.Column(db.String(255))
    status = db.Column(db.String(50))
