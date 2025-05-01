from flask import request
from bookish.models.book import Book
from bookish.models.user import User
from bookish.app import db
from flask import Blueprint


bookish = Blueprint('bookish', __name__)


@bookish.route('/healthcheck')
def health_check():
    return {"status": "OK"}


@bookish.route('/book', methods=['POST', 'GET'])
def get_all_books():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_example = Book(Title=data['title'], Author=data['author'], ISBN=data['isbn'], Quantity=data['quantity'])
            db.session.add(new_example)
            db.session.commit()
            return {"message": "New example has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        books = Book.query.all()
        results = [
                {
                    'id': book.id,
                    'title': book.Title,
                    'author': book.Author,
                    'isbn' : book.ISBN,
                    'quantity' : book.Quantity
                } for book in books]
        return {"books": results}
    else:
        return {"error" : "request method not supported"}


@bookish.route('/book/<id>', methods=['GET'])
def get_book_by_id(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "Book not found"}
    else:
        return {'id' : book.id, 'title': book.Title, 'author': book.Author, 'isbn' : book.ISBN, 'quantity' : book.Quantity}


@bookish.route('/user', methods=['POST', 'GET'])
def get_all_users():
    users = User.query.all()
    results = [
                {
                    'id': user.id,
                    'name': user.Name,
                    'limit': user.Limit,
                    'books': [{ 'title' : book.Title } for book in user.books]
                } for user in users]
    return {"users": results}


@bookish.route('/user/<int:id>', methods=['GET'])
def get_user_by_id(id):
    user = User.query.get(id)
    if user is None:
        return {"error": "User does not exist"}
    else:
        return {"id": user.id, "name": user.Name, "limit": user.Limit, "books": [{ 'title' : book.Title } for book in user.books]}
