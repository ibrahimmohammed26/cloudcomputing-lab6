from flask import Flask, request, Response, jsonify
import json

app = Flask(__name__)

def check_auth(username, password):
    return username == "username" and password == "password"

def need_auth():
    return Response("Login required", 401,
                    {"WWW-Authenticate": 'Basic realm="Login Required"'})

@app.route("/")
def index():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return need_auth()
    with open("records.json") as f:
        return jsonify(json.load(f))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
