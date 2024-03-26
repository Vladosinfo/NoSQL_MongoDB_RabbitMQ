from datetime import datetime

from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import ReferenceField, DateTimeField, EmbeddedDocumentField, ListField, StringField


class Author(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Quotes(Document):
    tags = ListField(StringField())
    # author = ReferenceField(EmbeddedDocumentField(Author))
    author = ReferenceField(Author)
    quote = StringField()
    meta = {'allow_inheritance': True}
