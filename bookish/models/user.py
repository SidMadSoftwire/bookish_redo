from bookish.app import db
from bookish.models.user_book import user_book

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String())
    Password = db.Column(db.String())
    Limit = db.Column(db.Integer())
    books = db.relationship('Book', secondary=user_book, back_populates='users')

    def __init__(self, name, limit):
        self.Name = name
        self.Limit = limit


    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'Name': self.Name,
            'Limit': self.Limit
        }
