from flask_restful import Resource
from flask import jsonify, request, abort
from app import users

def client_has_parcel(username):
    client_parcel = users.find({
        "username":username
    })[0]["Parcel"]
    return client_parcel

def client_exists(username):
    if users.find({"username": username}).count() == 0:
        return False
    else:
        return True

def check_user_type(username):
    if users.find({"username": username})[0]["client"]:
        return False
    else:
        return True

def parcel_delivered(username):
    users.update({
        "username":username
    }, {
        "$set":{
            "receive_parcel": True
        }
    })

class ParcelAPI(Resource):
    '''A Resource that manages user(teller/admin) registration'''
    def post(self):
        parcel_data = request.get_json()
