from flask import Flask, render_template, request, redirect, session
import user.models
import requests, json, random
from functools import wraps
import pymongo
from quotes import quote_api
from datetime import date

app = Flask(__name__)
app.secret_key = "verysecret123"
# database
client = pymongo.MongoClient("127.0.0.1", 27017)
db = client.user_login_system
col = db["journal"]
# decorators
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            return redirect("/")

    return wrap


@app.route("/")
def landingpage():
    return render_template("homepage.html", test1=quote_api()[0], test2=quote_api()[1])


@app.route("/login/")
def login():
    return render_template("login.html")


@app.route("/user/login", methods=["POST"])
def log():
    return user.models.User().login()


@app.route("/user/signup", methods=["POST"])
def signup():
    return user.models.User().signup()


@app.route("/user/signout/")
def signout():
    return user.models.User().signout()


@app.route("/sendinfo")
def register():
    return render_template("signup.html")


@app.route("/dashboard/")
@login_required
def dashboard():
    name = session["user"]["email"]
    if db.posts.find_one({"account": name}):
        log = db.posts.find_one({"account": name})["posts"]
        logdates = db.posts.find_one({"account": name})["dates"]
        return render_template("dashboard.html", log=log, day=logdates)
    return render_template("dashboard.html")


@app.route("/submitdata/", methods=["POST", "GET"])
@login_required
def usersubmitdata():
    data = "ORANGE JUICE"
    name = session["user"]["email"]
    day = date.today().strftime("%B %d, %Y")
    content = {"account": name, "posts": [], "dates": []}
    if db.posts.find_one({"account": name}):
        db.posts.update_one({"account": name}, {"$push": {"posts": data}})
        db.posts.update_one({"account": name}, {"$push": {"dates": day}})
    else:
        db.posts.insert_one(content)
        db.posts.update_one({"account": name}, {"$push": {"posts": data}})
        db.posts.update_one({"account": name}, {"$push": {"dates": day}})
    log = db.posts.find_one({"account": name})
    print(log["posts"])
    return redirect("/dashboard/")


if __name__ == "__main__":
    app.run(debug=True)