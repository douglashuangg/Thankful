from flask import Flask, render_template, request, redirect
import requests, json, random
from quotes.py import test1, test2

app = Flask(__name__)

@app.route('/')
def landingpage():

    return render_template('homepage.html', test1 = test1, test2 = test2)




if __name__ == '__main__':
    app.run(debug=True)