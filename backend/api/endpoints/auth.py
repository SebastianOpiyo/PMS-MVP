from flask import jsonify, request, abort
from app import users
from flask_restful import Resource
import bcrypt


def verify_password(username, password):
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

        user_exist = verify_password(username, password)
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
    '''A class that managed user sign in.'''
    pass

class ResendConfirmationAPI(Resource):
    '''Sends a confirmation link to mail upon registration.'''
    pass

class RequestPasswordResetAPI(Resource):
    pass

class PasswordChangeAPI(Resource):
    pass
