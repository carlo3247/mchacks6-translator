from flask import Flask
from flask import request
from twilio.twiml.voice_response import VoiceResponse

import urllib.request

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

app = Flask(__name__)

stt_client = speech.SpeechClient()

@app.route("/recorded", methods=['GET', 'POST'])
def recorded():
    # get url
    print('url: {}'.format(request.form['RecordingUrl']))
    url = request.form['RecordingUrl']

    # get .wav file
    audio_file = urllib.request.urlopen(url)
    content = audio_file.read()

    # stt using google cloud
    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(language_code='en-US')
    stt_response = stt_client.recognize(config, audio)

    print(stt_response[0].alternatives[0])

    response = VoiceResponse()
    response.say('Thank you')
    response.hangup()
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
