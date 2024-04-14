from mongoengine import connect
import configparser
import os


CONFIG_FILE = 'db/config.ini'


def db_connect(db_name=None, config = None):
    print(f"from db_connect: {os.getcwd()}")
    
    try:
        if config != None:
            config = config
        else:
            config = configparser.ConfigParser()
            config.read(CONFIG_FILE)
        mongo_user = config.get('DBCredentials', 'user')
        mongodb_pass = config.get('DBCredentials', 'pass')
        if db_name != None:
            db_name = db_name
        else:
            db_name = config.get('DBCredentials', 'db_name')
        domain = config.get('DBCredentials', 'domain')

        connect(host=f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority""", ssl=True)
        print('Connected to MongoDB')
    except Exception as e:
        print(f'An error occurred while connecting to MongoDB: {e}')    
