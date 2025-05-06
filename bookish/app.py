import os
from flask import Flask
from bookish.models import db, migrate



def create_app():
    app = Flask(__name__)

    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    import bookish.models.books
    import bookish.models.users
    import bookish.models.borrowed_books

    db.init_app(app)
    migrate.init_app(app, db)


    return app

