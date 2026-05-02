from flask import Flask,request,jsonify
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logging_middleware.logger import Log
app=Flask(__name__)
notifications=[]

@app.route('/notify',methods=['POST'])
def send_notification():
    input=request.json
    notification={
        'id':len(notifications)+1,
        'message':input['message'],
    }
    notifications.append(notification)
    Log("backend","info","service","Notification sent!")
    return jsonify(notification)

@app.route('/notifications')
def get_notification():
    Log("backend","info","handler","fetched notification!")
    return jsonify(notifications)

app.run(debug=True)