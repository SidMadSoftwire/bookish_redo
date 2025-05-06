from bookish.app import db


class Books(db.Model):
    # This sets the name of the table in the database
    __tablename__ = 'books'

    # Here we outline what columns we want in our database
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String())
    author = db.Column(db.String())
    isbn = db.Column(db.String(), unique=True)
    stock = db.Column(db.Integer)

    def __init__(self, title, author, isbn, stock):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.stock = stock

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'Title': self.title,
            'Author': self.author,
            'ISBN': self.isbn,
            'Stock': self.stock,
        }
