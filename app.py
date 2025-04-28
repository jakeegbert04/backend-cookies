from flask import Flask, jsonify, make_response, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route("/auth/login")
def auth_login():
    res = make_response(jsonify('cookies are set'))
    res.set_cookie('user', 'approved', expires="Wed 3 Feb 2030 20:45:00 UTC", path="/", secure=True, httponly=True, samesite="None")
    return res

@app.route("/am-i-approved")
def approval_process():
    auth = request.cookies.get("user")
    if auth == "approved":
        return make_response(jsonify("You are approved!"))
    return make_response(jsonify("You are not approved. Go get approved at /set-cookie"))

app.run(debug=True)