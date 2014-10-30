from flask import Flask
from flask import request
<<<<<<< HEAD
import os, sys
=======
from os import listdir
from os.path import isfile,join
>>>>>>> b5371568acf1edf9c33f9313832fe4ab9eaaee8d
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! YEEEEI!"

@app.route('/show')
def show_uploads():
    upFiles = [ f for f in listdir(./uploads/) if isfile(join(./uploads/, f)) ]
    return upFiles

@app.route('/listfiles')
def list():
    files = ""
    path = "./uploads"
    file = os.listdir(path)
    for i in file:
        files += i + " "
    return files + "\n"

  
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('./uploads/'+f.filename)
    return '',201
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


@app.route("/download", methods=['GET', 'POST'])
def download():
    if request.method == 'GET':
	f = request.files['file']
   	f.load('./upload/'+f.filename)
    return '', 201    	
