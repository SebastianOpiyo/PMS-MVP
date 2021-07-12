from flask import Flask, jsonify, request
from flask_restful import Api
from pymongo import MongoClient
import os

app = Flask(__name__)
API = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.PmsDatabase
users = db["Users"]
parcels =db["Parcels"]
payment = db["Payment"]

# APIs
from api.endpoints.auth import Register,SignInAPI, PasswordChangeAPI
from api.endpoints.parcel import RegisterParcel, TransferParcel
from api.endpoints.payment import PaymentAPI, GetAllPaymentRecords

# Api EndPoints Register
# Auth
API.add_resource(Register, '/register')
API.add_resource(SignInAPI, '/signin')
API.add_resource(PasswordChangeAPI, '/changePassword')

#Parcel
API.add_resource(RegisterParcel, '/registerParcel')
API.add_resource(TransferParcel, '/transferParcel')

# Payment
API.add_resource(PaymentAPI, '/payment')
API.add_resource(GetAllPaymentRecords, '/paymentRecords')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
