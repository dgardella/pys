# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request
from multiprocessing import Process
from threading import Thread
import time as t
import asyncio
import os
from datetime import datetime


path = "/tmp/testx/"

 
# creating a Flask app
app = Flask(__name__)

@app.route('/home/<int:num>', methods = ['GET'])
def disp(num):
 
    return jsonify({'data': num**2})
 
@app.route('/alive')
def start_task():
    def do_work(value):
        # do something that takes a long time
        #time.sleep(value)
        now = datetime.now() 
        #date_time = now.strftime("%m-%d-%Y-%H-%M-%S")
        date_time = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
        file_name = path + date_time
        print("I'm alive - get me token")
        with open(f'{file_name}.token', 'w') as f:
        #with open(f'{file_name}, 'w') as f:
            f.write('xxx')
        seconds = value
        for i in range(seconds):
            print(str(seconds-i) + " seconds remaining \n")
            t.sleep(1)
        print("Time is up - deleting token")
        import os
        os.remove(f'{file_name}.token')
        #return('hola')


    thread = Thread(target=do_work, kwargs={'value': request.args.get('value', 15)})
    thread.start()
    return 'started'



def check_wd ():
    while True:
        print ("Checking")
        sleep(10)


# driver function
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug = True)
    #
    # check_wd()
    #app.run(debug = True)