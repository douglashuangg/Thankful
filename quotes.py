import requests, json, random


def quote_api():
    # FOR QUOTES
    base_url = "https://type.fit/api/quotes"
    quotes_list = requests.get(base_url).json()
    authors = [name["author"] for name in quotes_list]
    quote_text = [name["text"] for name in quotes_list]
    test1 = random.choice(authors)
    test2 = random.choice(quote_text)
    print(test1, test2)
    l = [test1, test2]
    return l


print(quote_api())
