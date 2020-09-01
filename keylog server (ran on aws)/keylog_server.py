from flask import Flask, request
from datetime import datetime
from os import path
import re

app = Flask(__name__)

#@ = function decorator -------- flask function decorator that says call this function at this path
@app.route('/')
def homepage():
    return 'server'

#to test with curl - curl -X POST -H "Content-Type: application/json" localhost:5000/write --data "{\"name\":\"testname\",\"data\":\"testdata\"}"
@app.route('/write', methods=['POST'])
def write():
    #send data to server in format json 
    #parse the request
    args = request.get_json()
    
    #regex - subs everything not letter or number with blanks
    name = re.sub('[^a-zA-Z0-9]', '', args['name'])
    data = args['data']
    
    file = open(name + '.txt', 'a')
    file.write('\n')
    file.write(str(datetime.now()))
    file.write('\n')
    
    file.write(data)
    file.write('\n')
    file.close()
    
    return ('OK')

#name changes depending on which file
#<name> makes name a parameter in the func
@app.route('/read/<name>', methods=['GET'])
def read(name):
    name = re.sub('[^a-zA-Z0-9]', '', name)
    #no file exists first
    if not path.exists(name + '.txt'):
        return ('Not Found')
    #no else needed
    file = open(name + '.txt', 'r')
    data = file.read()
    file.close()
    
    #flask takes data and converts it to html by default
    #new lines in text dont convert to new lines in html
    #second arg doesnt convert text to html -------- dictionary / hashmap
    return (data, {'content-type': 'text'})

#ssh -i aws-josh.pem ubuntu@18.188.58.17 to login to server ---- run commands like scp
#scp to transfer files from one server to another ----- scp -i aws-josh.pem from from2 to)
#echo - print
#nano .bash_profile for alias
#reload bash config file using source on change or exit
#internet connection = port 80
#0.0.0.0 is public ip
