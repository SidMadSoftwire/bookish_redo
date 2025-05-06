from flask import request
from bookish.models.books import Books
from bookish.app import db
from flask import Blueprint


book_controller = Blueprint('book_controller', __name__)


@book_controller.route('/healthcheck')
def health_check():
    return {"status": "OK"}


@book_controller.route('/books', methods=['POST', 'GET'])
def handle_books():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()

            if 'title' in data and 'author' in data and 'isbn' in data and 'stock' in data:
                book = Books.query.filter(Books.isbn == data['isbn']).first()

                if book is None:
                    new_example = Books(title=data['title'], author=data['author'], isbn=data['isbn'], stock=data['stock'])
                    db.session.add(new_example)
                    db.session.commit()
                    return {"message": "New book entry has been created successfully."}
                elif book.title == data['title'] and book.author == data['author']:
                    Books.query.filter(Books.isbn == data['isbn']).update({'stock': Books.stock + data['stock']})
                    db.session.commit()
                    return {"message": "Book stock has been updated successfully."}
                else:
                    return {"error": "ISBN does not correspond to title or author."}

            else:
                return {"error": "A book entry needs a title, author, ISBN and an amount to add to stock."}

        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        books = Books.query.order_by("title").all()
        results = [{
                    'id': book.id,
                    'title': book.title,
                    'author': book.author,
                    'isbn' : book.isbn
                } for book in books]
        return {"catalogue": results}
    else:
        return {"error" : "request method not supported"}

