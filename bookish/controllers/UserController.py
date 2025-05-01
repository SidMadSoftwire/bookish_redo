from bookish.models.user import User
from flask import Blueprint
from bookish.wrappers.LoginWrapper import login_required

user_controller = Blueprint('user_controller', __name__)


@user_controller.route('/user', methods=['POST', 'GET'])
@login_required
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


@user_controller.route('/user/<int:id>', methods=['GET'])
@login_required
def get_user_by_id(id):
    user = User.query.get(id)
    if user is None:
        return {"error": "User does not exist"}
    else:
        return {"id": user.id, "name": user.Name, "limit": user.Limit, "books": [{ 'title' : book.Title } for book in user.books]}
