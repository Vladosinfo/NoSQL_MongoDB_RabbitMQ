from datetime import datetime
from bson import json_util
from mongoengine import EmbeddedDocument, connect, Document, CASCADE
from mongoengine.fields import ReferenceField, DateTimeField, EmbeddedDocumentField, ListField, StringField, DictField


class Author(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()
    meta = {"collection": "authors"}


class Quotes(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author)
    quote = StringField()

    meta = {"collection": "quotes"}
