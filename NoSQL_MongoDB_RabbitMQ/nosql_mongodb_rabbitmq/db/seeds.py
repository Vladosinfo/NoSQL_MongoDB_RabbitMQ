import db_connect
from models import Author, Quotes
import json

f_authors = '../data/authors.json'
f_quotes = '../data/quotes.json'

with open(f_quotes, "r") as qt:
    quotes = json.load(qt)

with open(f_authors, "r") as ath:
    aughors = json.load(ath)

auth_list = []
for auth in aughors:
    Author(fullname = auth['fullname'], 
        born_date = auth['born_date'],
        born_location = auth['born_location'],
            description = auth['description'])
    auth_list.append(auth)

for quot in quotes:
    auth = ""
    for auth_obj in auth_list:
        if auth_obj['fullname'] == quot['author']:
            auth = auth_obj
            break
        
    Quotes(tags = quot['tags'], 
            author = auth,
            quote = quot['quote']).save()    
