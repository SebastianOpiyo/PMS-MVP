from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import os

from pymongo import MongoClient

# APIs
from .api.endpoints.auth import Register


app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.PmsDatabase

users = db["Users"]


# Api EndPoints Register
# api.add_resource(Home, '/')
api.add_resource(Register, '/register')
# api.add_resource(SignUpAPI, '/getuser')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
