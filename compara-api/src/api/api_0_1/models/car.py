from model import *


class Car(Model, db.Model):
    __tablename__ = 'cars'

    name = db.Column(db.String(50))
    plate = db.Column(db.String(50))
