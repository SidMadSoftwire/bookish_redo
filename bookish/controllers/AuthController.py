from bookish.models.user import User
from flask import Blueprint, session
from flask import request


auth_controller = Blueprint('auth_controller', __name__)

@auth_controller.route('/auth', methods=['POST', 'GET'])
def user_login():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            user_name = data['user_name']
            if not User.query.filter_by(username=user_name).Any():
                return { "Error": "Invalid username" }, 401
            password = User.query.filter_by(username=user_name).first().password
            if data['password'] != password:
                return { "Error": "Invalid password" }, 401
            session['user_name'] = user_name
            return { "Success": True }, 200
    return { "Error": "Use POST to login" }, 401