from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    name = {
    "first_name": "Opiyo",
    "second_name": "Sebastian"
    }
    return jsonify(name)

@app.route('/authenticate', methods=["POST"])
def authenticate_user():
    userdata = request.get_data()
    return userdata


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True, port=80)
