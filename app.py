from flask import Flask, jsonify, request
import controllers
import android
import service


app = Flask("__main__")

app.register_blueprint(controllers.select)
app.register_blueprint(controllers.insert)
app.register_blueprint(android.android_api)
app.register_blueprint(service.serv)

@app.route('/api/', methods = ['POST', 'GET'])
def api() :

    return jsonify({
        'routes' : [
            {
                'name' : '/api/select',
                'description' : 'Select query interface, parms : An SQL query and its parameters'
            }, 
            {
                'name' : '/api/insert',
                'description' : 'A generic query interface for inserting documents'
            }
        ]
    })

app.run(port = 7000)