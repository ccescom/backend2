from flask import Blueprint, request, jsonify
from serv.sms import send_sms
from serv.translate import translate_text
from serv.voice import send_voice_call


serv = Blueprint("service", __name__)

@serv.route('/api/sms', methods = ['POST'])
def message():
    to_ = request.get_json()['to']
    payload = request.get_json()['payload']
    lng = request.get_json()['lang']

    #translate : 
    result_ln  = translate_text('en', lng, payload)

    send_sms(None, to_, result_ln, useDefault = True)
    
    for i in range(len(to_)) :
        to_[i] = '91' + to_[i]

    send_voice_call('./serv/creds.json', result_ln, lang = 'hi-IN', to = to_)

    return jsonify ({
        'success' : True
    })

