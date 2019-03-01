from flask import Blueprint , Flask, jsonify, request
from db_init import dbase

select  = Blueprint("select", __name__)

@select.route('/api/select', methods = ['POST'])
def select_() :

    query = request.get_json()['query']
    parameters = request.get_json()['parameters']

    print(parameters)

    result = dbase.select(query, parameters)
    
    return jsonify({
        'success' : True,
        'result' : result
    })

insert = Blueprint("insert", __name__) 

@insert.route('/api/insert', methods = ['POST'])
def insert_() :

    query = request.get_json()['query']
    parameters = request.get_json()['parameters']

    dbase.insert(query, parameters)

    return jsonify({
        'success' : True,
        'result' : 'Inserted'
    })

