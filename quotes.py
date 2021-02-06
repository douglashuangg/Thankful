import requests, json, random

def quote_api():
    #FOR QUOTES
    base_url = "https://goquotes-api.herokuapp.com/api/v1/"
    testing_response = requests.get(base_url + "/all/quotes").json()
    quotes_list = testing_response['quotes']
    authors = [name['author'] for name in quotes_list]
    quote_names = [name['text'] for name in quotes_list]
    test1 = random.choice(authors)
    test2 = random.choice(quote_names)
    return test1, test2

print(quote_api())
