import random
from wsgi import create_app
from bookish.models.books import Books


def test_adding_book():
    app = create_app()

    with app.app_context():
        rand = str(random.randrange(10000000, 10000000000))

        app.test_client().post("/books", json={
            "title": "A New Book",
            "author": "J. Doe",
            "isbn": rand,
            "stock": 2
        })

        book = Books.query.filter(Books.isbn == rand).first()
        assert book.title == "A New Book" and book.author == "J. Doe" and book.stock == 2

def test_updating_book():
    app = create_app()

    with app.app_context():
        book = Books.query.filter(Books.isbn == "0123456789").first()
        stock_before = book.stock

        app.test_client().post("/books", json={
            "title": "Test Book",
            "author": "J. Doe",
            "isbn": "0123456789",
            "stock": 3
        })

        stock_after = book.stock

        assert stock_after == stock_before + 3