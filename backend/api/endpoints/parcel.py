from flask_restful import Resource
from flask import request, jsonify
from app import users, parcels
from ..utils.utils import return_json

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
        return True
    else:
        return False

def agent_details(agent):
    if users.find({"agent": agent})[0]:
        return True
    else:
        return False

def parcel_delivered(username):
    users.update({
        "username":username
    }, {
        "$set":{
            "receive_parcel": True
        }
    })

class RegisterParcel(Resource):
    '''A Resource that manages user(teller/admin) registration'''
    def post(self):
        parcel_data = request.get_json()
        parcel_type = parcel_data["name"]
        weight = parcel_data["weight"]
        height = parcel_data["height"]
        sender = parcel_data["sender"]
        to_name = parcel_data["to_name"]
        to_phone = parcel_data["to_phone"]
        from_location = parcel_data["origin"]
        destination = parcel_data["location"]
        status = parcel_data["transfer"]
        user_exists = client_exists(sender) and check_user_type(sender)
        if not user_exists:
            return return_json(404, "Create new client first.")
        parcels.insert({
            "sender":sender,
            "parcel_type": parcel_type,
            "weight": weight,
            "height":height,
            "to":to_name,
            "to_phone": to_phone,
            "from_location":from_location,
            "destination":destination,
            "status":status
        })
        return return_json(201, "Resource created successfully.")

class TransferParcel(Resource):
    def post(self):
        parcel_data = request.get_json()
        depart_time = parcel_data["departure"]
        transport_means = parcel_data["transport"]
        sender= parcel_data["sender"]
        receiver = parcel_data["receiver"]
        agent_name = parcel_data["agentName"]
        destination = parcel_data["destination"]
        message = parcel_data["message"]
        sendNotification(agent_name, sender, receiver, message)
        transported = parcels.insert({
            "departure":depart_time,
            "means":transport_means,
            "sender":sender,
            "receiver":receiver,
            "agent":agent_name,
            "destination":destination,
            "message":message,
            "transported":True,
            "received":False
        })
        return jsonify(transported), return_json(201, "Resource successfully created!")

class ReceiveParcel(Resource):
    def post(self):
        transport_data = request.get_json()
        agent = transport_data["agent"]
        sender = transport_data["sender"]
        departure = transport_data["departure"]
        transported = transport_data["transported"]

        check_record = parcels.find({
            "agent":agent,
            "sender":sender,
            "departure":departure,
            "transported":transported
        })

        if not check_record:
            return return_json(200, "No records found!"), jsonify(check_record)
        else:
            parcels.update({
                "agent": agent,
                "sender": sender,
                "departure": departure,
                "transported": transported
            },
                {
                    "$set": {
                        "received": True
                    }
            })
        return return_json(201, "Parcel Received at Destination!")


def sendNotification(transporter:str, sender:str, reciver:str, message:str):
    # Write notification code here
    # We can integrate bulk sms too so that all parties get notified.
    pass