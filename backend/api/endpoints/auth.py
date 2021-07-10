from flask import Flask, jsonify, request


class SignUpAPI(Resource):
    '''A Resource that manages user(teller/admin) registration'''
    pass

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
