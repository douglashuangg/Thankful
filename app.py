from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def landingpage():
    return render_template('homepage.html')