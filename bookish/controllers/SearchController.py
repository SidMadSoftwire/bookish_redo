from flask import request
from bookish.models.books import Books
from flask import Blueprint


search_controller = Blueprint('search_controller', __name__)


@search_controller.route('/healthcheck')
def health_check():
    return {"status": "OK"}


@search_controller.route('/books/id:<int:id>', methods=['POST', 'GET'])
def find_by_id(id):
    if request.method == 'GET':
        book = Books.query.filter(Books.id == id).first()
        result = {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'isbn': book.isbn,
            'stock': book.stock
        }
        return {"book": result}
    else:
        return {"error": "request method not supported"}


@search_controller.route('/books/title:<title>', methods=['POST', 'GET'])
def search_by_title(title):
    if request.method == 'GET':
        books = Books.query.filter(Books.title == title).all()
        results = [{
            'id': book.id,
            'author': book.author,
            'isbn': book.isbn
        } for book in books]
        return {f"books titled {title}": results}
    else:
        return {"error" : "request method not supported"}


@search_controller.route('/books/author:<author>', methods=['POST', 'GET'])
def search_by_author(author):
    if request.method == 'GET':
        books = Books.query.filter(Books.author == author).all()
        results = [{
            'id': book.id,
            'title': book.title,
            'isbn': book.isbn
        } for book in books]
        return {f"books by {author}": results}
    else:
        return {"error": "request method not supported"}