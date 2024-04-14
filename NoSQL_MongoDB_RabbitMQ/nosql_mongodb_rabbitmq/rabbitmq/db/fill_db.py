from faker import Faker
import os
from nosql_mongodb_rabbitmq.db.db_connect import db_connect
from .models import Contact
import random
import configparser

NUMBER_CONTACST = 100


current_directory = os.getcwd()
path_two_levels_up = os.path.dirname(current_directory)
# path_two_levels_up = os.path.dirname(os.path.dirname(current_directory))

config = configparser.ConfigParser()
config_path = path_two_levels_up+"\db\config.ini"
config.read(config_path)

fake = Faker()
db_connect("contacts", config)

def get_fake_data(num_cont=100):
    fake_fullnames = []
    fake_emails = []
    fake_phones = []
    fake_methods = ["email", "SMS"]


    for _ in range(num_cont):
        fake_fullnames.append(fake.name())
    
    for _ in range(num_cont):
        fake_emails.append(fake.email())

    for _ in range(num_cont):
        fake_phones.append(fake.phone_number())

    
    return fake_fullnames, fake_emails, fake_phones, fake_methods



def fill_db(count_contacts):
    fullnames, emails, phones, methods = get_fake_data(count_contacts)
    list_contact_objects = []
    for i in range(count_contacts):
        contact_object = Contact(
                fullname = fullnames[i-1],
                email = emails[i-1],
                sent = False,
                phone = phones[i-1],
                send_method = methods[random.randint(0,1)]
            )
        obj = contact_object.save()
        list_contact_objects.append(obj)

    return list_contact_objects
