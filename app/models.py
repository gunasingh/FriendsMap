__author__ = 'Guna'

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    destinations = db.relationship('Destination', backref='traveller', lazy='dynamic')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Destination(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    addr_line1 = db.Column(db.String(140))
    addr_line2 = db.Column(db.String(140))
    addr_city = db.Column(db.String(140))
    addr_zip = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.addr_line1 + ", " + self.addr_line2 + ", " + self.addr_city)