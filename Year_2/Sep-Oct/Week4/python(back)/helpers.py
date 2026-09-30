import json

import argon2

def dbRead():
    try:
        with open(
            "db.json",
        ) as file:
            db = json.load(file)
            return db, None
    except FileNotFoundError as e:
        return None, f"ERROR: Database Not found \nErr: {e}"


def confPass(data):
    ph = argon2.PasswordHasher()
    if data["password"] != data["confPassword"]:
        return None, "Your passwords did not match 3:"
    elif data["password"] == data["confPassword"]:
        hashPass = ph.hash(data["password"])
        return hashPass, None
    else:
        return None, "SOMETHING WENT VERY WRONG"

def verLogin(data):
    db, _ = dbRead()
    if db == None:
        return None, "db read failed"

    ph = argon2.PasswordHasher()

    for i in db:
        if data["username"] == i["username"]:
            try:
                ph.verify(i["password"], data["password"])
            except(argon2.exceptions.VerifyMismatchError,argon2.exceptions.InvalidHash,) as e:
                return False, e
            else:
                return True, None
