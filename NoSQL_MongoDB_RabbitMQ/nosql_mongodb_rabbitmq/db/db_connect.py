from mongoengine import connect
import configparser
import os

# debug connection
# D:\git_python\NoSQL_MongoDB_RabbitMQ
CONFIG_FILE = './NoSQL_MongoDB_RabbitMQ/nosql_mongodb_rabbitmq/db/config.ini'
# normal connection
# D:\git_python\NoSQL_MongoDB_RabbitMQ\NoSQL_MongoDB_RabbitMQ\nosql_mongodb_rabbitmq
# CONFIG_FILE = 'db/config.ini'
# if connect from 'db' folder ( when starting seeds.py - for example )
# CONFIG_FILE = 'config.ini'

def db_connect():
    print(os.getcwd())
    try:
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE)
        mongo_user = config.get('DBCredentials', 'user')
        mongodb_pass = config.get('DBCredentials', 'pass')
        db_name = config.get('DBCredentials', 'db_name')
        domain = config.get('DBCredentials', 'domain')

        # connect to cluster on AtlasDB with connection string
        #mongodb+srv://vladyslav:<password>@vprogdb.wstfbh3.mongodb.net/
        connect(host=f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority""", ssl=True)
        print('Connected to MongoDB')
    except Exception as e:
        print(f'An error occurred while connecting to MongoDB: {e}')    




# from mongoengine import connect #, ConnectionError
# import configparser
# def db_connect():
#     try:
#         config = configparser.ConfigParser()
#         config.read('config.ini')
#         mongo_user = config.get('DB', 'user')
#         mongodb_pass = config.get('DB', 'pass')
#         db_name = config.get('DB', 'db_name')
#         domain = config.get('DB', 'domain')
#         connect(
#             db=db_name,
#             username=mongo_user,
#             password=mongodb_pass,
#             host=f'mongodb+srv://{domain}',
#             authentication_source='admin',
#             ssl=True,
#             retryWrites=True,
#         )
#         print('Connected to MongoDB')
#     except Exception as e:
#         print(f'An error occurred while connecting to MongoDB: {e}')    
