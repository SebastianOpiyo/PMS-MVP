from app import users
from flask import jsonify, request, abort
from ..utils.utils import return_json
from flask_restful import Resource
import bcrypt

def authenticate_user(username, password):
    hashed_pw = users.find({
    "username":username
    })[0]["password"]
    if bcrypt.hashpw(password.encode('utf8'), hashed_pw) == hashed_pw:
        return True
    return False

def verify_user(username):
    if users.find({"username":username}).count()==0:
        return False
    else:
        return True

class Register(Resource):
    '''A Resource that manages user(teller/admin) registration'''
    def post(self):
        client_data = request.get_json()
        username = client_data['username']
        password = client_data['password']
        usertype = client_data['usertype']
        if username is None or password is None:
            abort(400) # missing arguments

        user_exist = verify_user(username)
        if user_exist:
            ret_response = {
                "status": 400,
                "msg":"Username already taken, choose another!"
            }
            return jsonify(ret_response)

        hashed_pw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        users.insert({
            "username":username,
            "password":hashed_pw,
            "usertype": usertype
        })

        ret_response = {
            "status": 201,
            "msg":"Successfully created user"
        }
        return jsonify(ret_response)

    def get(self):
        client_data = request.get_json()
        username = client_data['username']
        valid_user = verify_user(username)

        if not valid_user:
            return_response = {
            "status": 403,
            "msg":"Username already taken, choose another!"
            }
            return jsonify(return_response)
        # Return user details
        user_details = users.find({"username":username})[0]
        ret_response = {
        "status": 200,
        "user_details": user_details,
        "msg":"Success!"
        }
        return jsonify(ret_response)


class SignInAPI(Resource):
    '''A class that manages user sign in.'''
    def post(self):
        user_data = request.get_json()
        username = user_data["username"]
        password = user_data["password"]

        is_user = authenticate_user(username,password)
        if not is_user:
            return return_json(403, "Forbidden from this resource.")
        user_details = users.find({
            "username":username
        },{
            "password":0
        })[0]
        return return_json(200, user_details)

class GetUsers(Resource):
    def get(self):
        registered_users = users.find({},{"password":0})

        if not registered_users:
            return jsonify({
                "status":200,
                "msg": "No records in the database."
            })
        else:
            return return_json(200, "Records found!"), jsonify(registered_users)

class PasswordChangeAPI(Resource):

    def post(self):
        user_data = request.get_json()
        username = user_data["username"]
        password = user_data["password"]

        users.update({
            "username": username
        }, {
            "$set": {
                "password": password
            }
        })

    class ResendConfirmationAPI(Resource):
        '''Sends a confirmation link to mail upon registration.'''
        # todo
        pass

    class RequestPasswordResetAPI(Resource):
        # todo
        pass

