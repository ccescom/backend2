import requests
import json

class YandexTranslate() :

    def __init__(self , source , dest) :

        self.parms = {
            "SOURCE_LANG" : source,
            "DEST_LANG" : dest,
            "API_KEY" : "trnsl.1.1.20190217T152435Z.104eba8e7fd552cf.5cbbc0754ee8765cc0e2d7bb89c65c253ff07058",
            "TEXT" : '',
            "REQ_URL" : 'https://translate.yandex.net/api/v1.5/tr.json/translate'
        } 

        self.result = None

    def translate(self, text) :
        self.parms["TEXT"] = text

        request = requests.get(
            self.parms['REQ_URL'],
            params = {
                "key" : self.parms["API_KEY"],
                "text" : self.parms["TEXT"],
                "lang" : self.parms["SOURCE_LANG"] + "-" + self.parms["DEST_LANG"]
            }
        )

        self.result = json.loads(request.text)
    
    def get_error_code(self):
        return self.result['code']
    
    def get_translated_text(self):
        return self.result['text']


def translate_text(src, dst, text):

    tr = YandexTranslate(src, dst)
    tr.translate(text)

    return tr.get_translated_text()[0] if tr.get_error_code() == 200 else "Error"

