from bookish.app import db


class BorrowedBooks(db.Model):
    # This sets the name of the table in the database
    __tablename__ = 'borrowed_books'

    # Here we outline what columns we want in our database
    id = db.Column(db.Integer, db.ForeignKey('books.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    due_date = db.Column(db.Date)

    def __init__(self, user_id, due_date):
        self.user_id = user_id
        self.due_date = due_date

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'Title': self.Title,
            'Author': self.Author,
            'ISBN': self.ISBN,
            'Quantity': self.Quantity,
        }
