import requests, json, random

def quote_api():
    # FOR QUOTES
    new_dict = {}
    base_url = "https://type.fit/api/quotes"
    quotes_list = requests.get(base_url).json()
    authors = [name["author"] for name in quotes_list]
    quote_text = [name["text"] for name in quotes_list]
    for author, quote in zip(authors, quote_text):
        new_dict.update({quote: author})
    testing = random.choice(list(new_dict.items()))
    test1 = ('"'+testing[0]+ '"' + "--"+testing[1]+'"')
    l = [test1]
    return l


print(quote_api())
