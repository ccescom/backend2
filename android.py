from flask import Blueprint, jsonify, request
from db_init import dbase

android_api = Blueprint("android_api", __name__)

@android_api.route('/api/android/login', methods = ['POST'])
def android_login() :

    query = "select FeederID, FarmerID from Farmer where Mobile =:Mobile"

    result = dbase.select(query, {
        "Mobile" : request.get_json()['Mobile']
    })

    print(result)
    if len(result) == 0 :

        return jsonify({
           'success' : True,
            'login' : False,
            'FarmerID' : None,
            'FeederID' : None
        })
    
    return jsonify({
        'success' : True,
        'login' : True,
        'FarmerID' : result[0]['FarmerID'],
        'FeederID' : result[0]['FeederID'],
        'Farmer_Name' : result[0]['Farmer_Name'],
        'Mobile' : result[0]['Mobile'],
        'Acres' : result[0]['Land_Size']
    })

@android_api.route('/api/android/get_schedule', methods = ['POST'])
def android_schedule() :

    feeder_id = request.get_json()['FeederID']

    query = "select * from Schedule where LineID=:FeederID"

    result = dbase.select(query, {
        "FeederID" : feeder_id
    })

    print(result)

    return jsonify({
        "success" : True,
        "result" : result[0]
    })

