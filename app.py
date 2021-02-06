from flask import Flask, render_template, request, redirect
import requests, json, random

app = Flask(__name__)

@app.route('/')
def landingpage():
    base_url = "https://goquotes-api.herokuapp.com/api/v1/"
    testing_response = requests.get(base_url + "/all/quotes").json()
    quotes_list = testing_response['quotes']
    authors = [name['author'] for name in quotes_list]
    quote_names = [name['text'] for name in quotes_list]
    test1 = random.choice(authors)
    test2 = random.choice(quote_names)

    return render_template('homepage.html', test_author = test1, test2 = test2)

if __name__ == '__main__':
    app.run(debug=True)