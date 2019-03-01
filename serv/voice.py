import boto3
import time
import nexmo
import json
from threading import Thread


class Voice(Thread):

    def __init__(self, data={}, text='', lang='hi-IN', number = '9611818690'):
        Thread.__init__(self)
        self.access_key_id = data['access_key_id']
        self.secret_access_key = data['secret_access_key']
        self.application_id = data['application_id']
        self.private_key_path = data['private_key_path']
        self.nexmo_client = nexmo.Client(
            application_id= self.application_id, private_key= self.private_key_path)
        self.polly_client = boto3.Session(
            aws_access_key_id= self.access_key_id, aws_secret_access_key= self.secret_access_key, region_name="ap-south-1").client('polly')
        self.lang = lang
        self.text = text
        self.number = number

    def run(self):

        response = self.polly_client.start_speech_synthesis_task(LanguageCode=self.lang, VoiceId='Aditi', OutputS3BucketName='sih-polly-test', OutputFormat='mp3', Text=self.text)
        status = ""
        taskId = response['SynthesisTask']['TaskId']

        while status != "completed":
            task_status = self.polly_client.get_speech_synthesis_task(TaskId=taskId)  # get the synthesis status from the client
            new_status = task_status['SynthesisTask']['TaskStatus']
            print('new Status is {}'.format(new_status))
            status = new_status  # update new status
            if(status == "completed"):
                break
            else:
                time.sleep(1)
        
        stream_url_array = []
        stream_url = response['SynthesisTask']['OutputUri'] #Gives the s3 file url
        stream_url_array.append(stream_url) #push url to array

        nexmo_response = self.nexmo_client.create_call({
            'to': [{'type': 'phone','number': self.number}],
            'from': {'type': 'phone','number':'12013816084'},
            'ncco': [{
                'action': 'stream',
                'streamUrl': stream_url_array
            }]
        })

        print(nexmo_response)


def send_voice_call(creds_file, text , lang, to) :

    creds = json.load(open(creds_file, 'r'))

    for number in to : 

        caller = Voice(data = creds, text = text, lang = lang, number = number)

        caller.start()




#send_voice_call('../creds.json', 'यह एक बहुत लंबा संदेश है जिसे मैं यह सुनिश्चित करने के लिए परीक्षण कर रहा हूं कि वार्तालाप स्ट्रीमिंग सही काम कर रही है जैसा कि मैंने सोचा था कि यह काम करेगा, यदि नहीं तो मुझे यह सुनिश्चित करना चाहिए कि यह काम करता है', lang = 'hi-IN', to = ['919611818690'])Se