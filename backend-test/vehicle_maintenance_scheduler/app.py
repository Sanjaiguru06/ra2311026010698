from flask import Flask,request,jsonify
from datetime import datetime,timedelta
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logging_middleware.logger import Log
app=Flask(__name__)
vehicles=[]

@app.route('/vehicles',methods=['POST'])
def add_vehicle():
    data=request.json
    vehicle={
        "id":len(vehicles)+1,
        "name":data['name'],
        "last_service":data["last_service"]
    }
    vehicles.append(vehicle)
    Log("backend","info","handler","vehicle added")
    return jsonify(vehicle)

@app.route('/vehicles')
def get_vehicles():
    Log("backend","info","handler","vehicle added")
    return jsonify(vehicles)

@app.route('/schedule',methods=['POST'])
def schedule_service():
    input=request.json
    for i in vehicles:
        if i['id']==input['vehicle_id']:
            last_date=datetime.strptime(i['last_service'],'%Y-%m-%d')
            next_date=last_date+timedelta(days=input['service_interval_days'])
            i['next_service']=next_date.strftime('%Y-%m-%d')

            Log("backend","info","services","service scheduled")
            return jsonify(i)
    
    Log("backend","error","handler","vehicle not found!")
    return jsonify({"message":"vehicle not found!"}),404


@app.route('/due-services')
def get_dueservices():
    today=datetime.today()
    result=[]
    for i in vehicles:
        if "next_service" in i:
            next_date=datetime.strptime(i['next_service'],'%Y-%m-%d')
            if next_date<=today:
                result.append(i)
            
    Log("backend","info","service","fetched due service!")
    return jsonify(result)

app.run(debug=True)
