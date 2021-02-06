
from flask import Flask, render_template, request, redirect, session
import user.models
import requests, json, random
from functools import wraps
import pymongo
from quotes import quote_api
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.secret_key = "verysecret123"
# database
client = pymongo.MongoClient("127.0.0.1", 27017)
db = client.user_login_system
# decorators
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            return redirect("/")
    return wrap

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

#database
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def __repr__(self): #recognize created new blogpost
        return 'Blog post' + str(self.id)

all_posts = [
    {
        'title': 'Post 1',
        'content': 'This is content'
    },
    {
        'title': 'Post 1',
        'content': 'This is content'
    }
]

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


@app.route("/posts", methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        new_post = BlogPost(title=post_title, content=post_content)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template("posts.html", posts=all_posts)
        

#@app.route("/dashboard/", methods=['POST'])
#@login_required
#def gratitudes(text):



if __name__ == "__main__":
    app.run(debug=True)