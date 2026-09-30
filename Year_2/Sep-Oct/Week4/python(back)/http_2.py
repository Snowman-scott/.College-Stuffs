import json

import argon2
from flask import Flask, request
from helpers import confPass, dbRead, verLogin

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Hello world"

@app.route("/register", methods=["POST"])
def register():
    data = request.form
    required = ("username","email","age","password","confPassword")
    missing = [k for k in required if not data.get(k)]
    if missing:
        return f"You were missing: {', '.join(missing)}"
    user = data["username"]
    em = data["email"]
    age = data["age"]
    passw, err = confPass(data)
    if err != None:
        return err
    newEntry = {"username": user, "email": em, "age": age, "password":passw}
    db, err = dbRead()
    if db == None:
        return f"db read failed with {err}"
    db.append(newEntry)

    with open("db.json", "w") as f:
        json.dump(db, f)
    return "valid entry : Data in db"

@app.route("/login", methods=["POST"])
def login():
    data = request.form
    required = ("username", "password")
    missing = [k for k in required if not data.get(k)]
    if missing:
        return f"You were missing: {', '.join(missing)}"
    user, err = verLogin(data)
    if user == 1:
        return f"{user} logged In"
    elif err:
        return f"login Error: {err}"

@app.route("/change-password", methods=["POST"])
def passChange():
    data = request.form
    required = ("Username","curPass","newPass","confPass")
    missing = [k for k in required if not data.get(k)]
    if missing:
        return f"You were missing: {', '.join(missing)}"
    user = data["username"]
    curPass = data["currPass"]
    newPass = data["newPass"]
    confPass = data["confPass"]



if __name__ == "__main__":
    app.run(debug=True, port=5001)
