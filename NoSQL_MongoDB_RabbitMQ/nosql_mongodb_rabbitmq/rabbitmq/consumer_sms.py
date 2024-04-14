import pika
import os
import time
import json
from bson import ObjectId
from nosql_mongodb_rabbitmq.db.db_connect import db_connect
from db.models import Contact
import configparser


current_directory = os.getcwd()
path_two_levels_up = os.path.dirname(current_directory)

config = configparser.ConfigParser()
config_path = path_two_levels_up+"\db\config.ini"
config.read(config_path)
db_connect("contacts", config)


credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='task_sms', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    message = json.loads(body.decode())
    print(f" [x] Received {message['fullname']} | phone: {message['phone']}")

    contact = Contact.objects(id=ObjectId(message['id']))
    contact.update(sent=True)

    print(f" [x] Done: {method.delivery_tag}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_sms', on_message_callback=callback)


if __name__ == '__main__':
    channel.start_consuming()
