from flask import Flask
from flask import request
from os import listdir
from os.path import isfile,join
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! YEEEEI!"

@app.route('/show')
def show_uploads():
    upFiles = [ f for f in listdir(./uploads/) if isfile(join(./uploads/, f)) ]
    return upFiles

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
