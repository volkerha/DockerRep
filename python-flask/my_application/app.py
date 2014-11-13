from flask import Flask
from flask import request
import os, sys
#import boto
import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/createQueue')
def createQ():
    conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id='AKIAIR7EH3TNSTDUCWKA', aws_secret_access_key='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')
    q = conn.create_queue("queue_jabba")
    #write 1 message to queue
    m = Message()
    m.set_body('first message')
    q.write(m)
    #write 100 messages to queue
    for x in range(1, 100):
        mx = Message()
        mx.set_body('Message'+x)
        q.write(mx)
    #read message from queue
    rs = q.get_messages()
    mread = rs[0]
    mread.get_body()
    #delete message from queue
    q.delete_message(m)
    return mread
  
@app.route('/listqueues')
def listQueues():
    conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id='AKIAIR7EH3TNSTDUCWKV', aws_secret_access_key='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')
    rs = conn.get_all_queues()
    qString = ""
    for q in rs:
        qString += q.id + "\n"
    return qString
  
@app.route('/listfiles')
def list():
    files = ""
    path = "./uploads"
    file = os.listdir(path)
    for i in file:
        files += i + " "
    return files + "\n"
  
@app.route('/euler1')
def euler1():
    sum = 0
    const1 = 3
    const2 = 5
    counter = 1
    while(counter < 1000):
    #multiple of 3 or 5? add to sum
        if (counter % const1 == 0 or counter % const2 == 0):
            sum += counter
        counter += 1
    return str(sum)
  
@app.route('/euler2')
def euler2():
    fib1 = 1
    fib2 = 2
    tmp = 2
    sum = 0
    while fib2 < 4000000:
    #even fib? add to sum
        if fib2 % 2 == 0:
            sum += fib2
        #swap fib to calc next fib
        tmp = fib2
        fib2 += fib1
        fib1 = tmp
    return str(sum)
  
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('./uploads/'+f.filename)
    return '',201
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
