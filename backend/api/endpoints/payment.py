from flask import Flask, jsonify, request
from flask_restful import Resource
from ..utils.utils import return_json
from app import payment

class PaymentAPI(Resource):
    '''A Resource that manages user(teller/admin) registration'''

    def post(self):
        parcel_data = request.get_json()
        username = parcel_data["username"]
        receiver = parcel_data["receiver"]
        parcel_tag_name = parcel_data["name"]
        parcel_weight = parcel_data["weight"]
        parcel_from = parcel_data["origin"]
        parcel_to = parcel_data["destination"]
        amount = parcel_data["amount"]
        payment_type = parcel_data["payment_type"]
        payment.insert({
            "username":username,
            "receiver_name":receiver,
            "weight":parcel_weight,
            "parcel_name":parcel_tag_name,
            "origin":parcel_from,
            "destination": parcel_to,
            "amount_paid":amount,
            "payment_type":payment_type
        })
        return return_json(201, "Payment Successful")

    def get(self):
        payment_data = request.get_json()
        username = payment_data["username"]
        user_record = payment.find({
            "username":username
        })[0]

        if not username:
            return return_json(200, "No records")
        else:
            return jsonify(user_record), return_json(200, "Records found!")

class GetAllPaymentRecords(Resource):
    def get(self):
        payment_records = payment.find()

        if not payment_records:
            return jsonify({
                "status": 200,
                "msg": "No records found!."
            })
        else:
            return return_json(200, "Records found!"), jsonify(payment_records)

class GenerateReceipt(Resource):
    """Generate receipt after payment has been made!"""
    #Todo
    pass

