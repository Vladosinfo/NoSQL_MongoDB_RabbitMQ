from db_connect import db_connect
from models import Author, Quotes
import json
import os
import configparser

current_directory = os.getcwd()
config = configparser.ConfigParser()
config_path = current_directory+"\config.ini"
config.read(config_path)

db_connect(None, config)

f_authors = '../data/authors.json'
f_quotes = '../data/quotes.json'


with open(f_quotes, "r", encoding="utf-8") as qt:
    quotes = json.load(qt)

with open(f_authors, "r", encoding="utf-8") as ath:
    authors = json.load(ath)


author_dict = {}
for auth in authors:
    author_object = Author(
            fullname = auth['fullname'],
            born_date = auth['born_date'],
            born_location = auth['born_location'],
            description = auth['description']
        )
    author_object.save()
    author_dict[auth['fullname']] = author_object


for quot in quotes:
    auth = ""
    author_obj_name = author_dict.get(quot['author'])
    if author_obj_name:
        Quotes(
                tags = quot['tags'], 
                author = author_obj_name,
                quote = quot['quote'][1:-1]).save()
        