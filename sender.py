#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='crawler')

channel.basic_publish(exchange='', routing_key='crawler',body='Hello World!')
channel.basic_publish(exchange='', routing_key='crawler',body='Hello World!')
channel.basic_publish(exchange='', routing_key='crawler',body='Hello World!')
channel.basic_publish(exchange='', routing_key='crawler',body='Hello World!')
channel.basic_publish(exchange='', routing_key='crawler',body='Hello World!')
channel.basic_publish(exchange='', routing_key='crawler',body='Hello World!')
print " [x] Sent 'Hello World!'"
connection.close()
