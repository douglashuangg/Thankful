import requests, json, random

def quote_api():
    base_url = "https://goquotes-api.herokuapp.com/api/v1/"
    testing_response = requests.get(base_url + "/all/quotes").json()

    #quotes_list = testing_response
    #quotes = [quote['text'] for quote in testing_response]
    quotes_list = testing_response['quotes']
    authors = [name['author'] for name in quotes_list]
    quote_names = [name['text'] for name in quotes_list]
    return(random.choice(quote_names) + random.choice(authors))

# print(quotes_list)
#titles = [title['name']['text'] for title in testing_response for name in title] 
    #return titles
#print(testing_response)


print(quote_api())
