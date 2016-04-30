#!/usr/bin/env python
import pika
import threading

def callback(ch, method, properties, body):
    print "channel Received " + str(ch)
    print "Thread Received %r" % (body,)



def worker() :
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    print channel
    channel.queue_declare(queue='crawler')
    
    channel.basic_consume(callback, queue='crawler', no_ack=False)
    channel.start_consuming()

threads = []
for i in range(1,5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
