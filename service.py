from flask import Blueprint, request, jsonify
from services import sms, voice, translate


serv = Blueprint("service", __name__)

@serv.route('/api/sms', methods = ['POST'])
def message():
    to_ = request.get_json()['to']
    payload = request.get_json()['payload']
    lng = request.get_json()['lang']

    #translate : 
    result_ln  = translate.yandex_translate('en', lng, payload)

    sms.send_sms(None, to_, result_ln, useDefault = True)
    
    for i in range(len(to_)) :
        to_[i] = '91' + to_[i]

    voice.make_call('./services/creds.json', result_ln, lang = 'hi-IN', to = to_)

    return jsonify ({
        'success' : True
    })

