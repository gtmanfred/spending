from .app import db

class Receipts(db.Model):
    __tablename__ = 'receipts'
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String())
    price = db.Column(db.Float(precision=2, asdecimal=True))
    date = db.Column(db.DateTime())

    def __init__(self, location, price):
        self.location = location
        self.price = price
        self.date = datetime

    def __repr__(self):
        return '<id {}>'.format(self.id)
