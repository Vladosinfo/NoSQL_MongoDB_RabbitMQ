from mongoengine import Document
from mongoengine.fields import StringField, BooleanField


class Contact(Document):
    fullname = StringField()
    email = StringField()
    sent = BooleanField(default=False)
    phone = StringField()
    send_method = StringField()
    meta = {"collection": "сontacts"}
