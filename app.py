from flask import Flask, render_template, request, redirect
import requests, json, random
from quotes import quote_api

app = Flask(__name__)


@app.route("/")
def landingpage():
    return render_template("homepage.html", test1=quote_api()[0], test2=quote_api()[1])


if __name__ == "__main__":
    app.run(debug=True)