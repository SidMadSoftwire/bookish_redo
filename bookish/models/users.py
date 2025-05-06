from bookish.app import db


class Users(db.Model):
    # This sets the name of the table in the database
    __tablename__ = 'users'

    # Here we outline what columns we want in our database
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'Username': self.username,
            'Password': self.password,
        }
