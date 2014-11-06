from flask import Flask
from flask import request
import os, sys
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

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
