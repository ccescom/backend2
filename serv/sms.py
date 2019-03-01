import requests
from threading import Thread
import json

default = {
        "COUNTRY" : 91,
        "SENDER" : "SIHTES",
        "ROUTE" : 4,
        "AUTH_KEY" : "263509AMoDWqDn5c6a74e8"
}

class SMS(Thread):

    def __init__(self, parms, mobiles, text) :

        Thread.__init__(self)

        self.country = parms['COUNTRY']
        self.sender = parms['SENDER']
        self.route = parms['ROUTE']
        self.mobiles = mobiles
        self.authkey = parms['AUTH_KEY']
        self.message = text

        self.URL = "http://api.msg91.com/api/sendhttp.php"

    
    def run(self):

        parms = {
            "country" :  self.country,
            "sender" : self.sender,
            "route" : self.route,
            "mobiles" : self.mobiles,
            "authkey" : self.authkey,
            "message" : self.message,
            "unicode" : 1
        }

        result = requests.get(self.URL, params = parms)

        print(result.text)



#test:
def send_sms(credentials, numbers, text, useDefault = True) :

    if useDefault : 

        SMS(default, numbers, text).start()
    
    else : 

        SMS(credentials, numbers, text).start()



