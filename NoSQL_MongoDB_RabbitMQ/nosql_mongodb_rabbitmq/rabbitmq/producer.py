import pika
from db.fill_db import fill_db
from datetime import datetime
import sys
import json
import logging

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='task_contact', exchange_type='direct')

try:
    channel.queue_declare(queue='task_email', durable=True)
    channel.queue_bind(exchange='task_contact', queue='task_email')
except Exception as e:
    # logger.error("Error creating task_email queue or binding: %s", str(e))
    print(e)

try:
    channel.queue_declare(queue='task_sms', durable=True)
    channel.queue_bind(exchange='task_contact', queue='task_sms')
except Exception as e:
    # logger.error("Error creating task_sms queue or binding: %s", str(e))
    print(e)


def main(contact_list_obj):
    for cont in contact_list_obj:
        contact = {
            "id": str(cont.id),
            "fullname": cont.fullname,
            "email": cont.email,
            "phone": cont.phone,
            "send_method": cont.send_method
        }


        if cont.send_method == 'email':
            channel.basic_publish(
                exchange='task_contact',
                routing_key='task_email',
                body=json.dumps(contact).encode(),
                # body=cont.id,
                properties=pika.BasicProperties(
                    delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
                ))
            print(" [x] Sent task_email queue %r" % contact)
            # print(" [x] Sent send_email queue %r | ObjectID:" % cont.id)
        else:
            channel.basic_publish(
                exchange='task_contact',
                routing_key='task_sms',
                body=json.dumps(contact).encode(),
                # body=cont.id,
                properties=pika.BasicProperties(
                    delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
                ))
            print(" [x] Sent task_sms queue %r" % contact)
            # print(" [x] Sent send_sms queue %r | ObjectID:" % cont.id)
            
    connection.close()
    
    
if __name__ == '__main__':
    main(fill_db(100))
