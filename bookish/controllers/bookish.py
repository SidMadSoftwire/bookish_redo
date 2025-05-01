from flask import request
from bookish.models.book import Book
from bookish.app import db
from flask import Blueprint


bookish = Blueprint('bookish', __name__)


@bookish.route('/healthcheck')
def health_check():
    return {"status": "OK"}


@bookish.route('/book', methods=['POST', 'GET'])
def handle_example():
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
        examples = Book.query.all()
        results = [
                {
                    'id': example.id,
                    'title': example.Title,
                    'author': example.Author,
                    'isbn' : example.ISBN,
                    'quantity' : example.Quantity
                } for example in examples]
        return {"examples": results}
    else:
        return {"error" : "request method not supported"}