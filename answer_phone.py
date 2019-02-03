from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

from flask import Flask
from flask import request
from twilio.twiml.voice_response import VoiceResponse

import urllib.request
import time

app = Flask(__name__)
stt_client = speech.SpeechClient()

britney = """"Oh baby, baby
Oh baby, baby
Oh baby, baby, how was I supposed to know
That something wasn't right here
Oh baby, baby, I shouldn't have let you go
And now you're out of sight, yeah
Show me how want it to be
Tell me baby 'cause I need to know now, oh because
My loneliness is killing me (and I)
I must confess I still believe (still believe)
When I'm not with you I lose my mind
Give me a sign
Hit me baby one more time"""

@app.route("/recorded", methods=['GET', 'POST'])
def recorded():
    if(request.form['CallStatus'] == 'completed':
        return

    # get url
    url = request.form['RecordingUrl']

    print('---')
    print(url)
    print('---')

    # maybe this works
    time.sleep(0.5)

    # get .wav file
    audio_file = urllib.request.urlopen(url)
    content = audio_file.read()

    # stt using google cloud
    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(language_code='en-US')
    stt_response = stt_client.recognize(config, audio)

    if len(stt_response.results) > 0:
        text = stt_response.results[0].alternatives[0].transcript
        confidence = stt_response.results[0].alternatives[0].confidence
    else:
        response.say('Sorry, I did not get that. Please try again.', voice='alice', language='en-US')
        response.record(action='/recorded', timeout=2, trim='trim-silence')
        return str(response)

    print('---')
    print(text)
    print(confidence)
    print('---')

    response = VoiceResponse()
    if text.__contains__('Britney'):
        response.say(britney, voice='alice', language='en-US')
    else:
        response.say(text, voice='alice', language='en-US')
        response.record(action='/recorded', timeout=2, trim='trim-silence')
    # response.hangup()
    return str(response)

# this is the entry point of a call
@app.route("/answer", methods=['GET', 'POST'])
def answer():
    response = VoiceResponse()
    response.say('Hello, Please leave a message after the beep.')
    response.record(action='/recorded', timeout=2, trim='trim-silence')
    return str(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80,debug=True)
