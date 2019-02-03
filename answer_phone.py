from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

from flask import Flask
from flask import request
from twilio.twiml.voice_response import VoiceResponse

import urllib.request
import time
import langaugeIdentifier
import watson

app = Flask(__name__)
stt_client = speech.SpeechClient()

twilio_timeout = 2
first_lang = 'en-US'
second_lang = ''

def speech_to_text(audio_content, lang):
    # stt using google cloud
    audio = types.RecognitionAudio(content=audio_content)
    config = types.RecognitionConfig(language_code=lang)
    stt_response = stt_client.recognize(config, audio)
    text = ''
    confidence 0
    if len(stt_response.results) > 0:
        text = stt_response.results[0].alternatives[0].transcript
    return text, confidence

def get_higher_confidence(content):
    textA, confidenceA = speech_to_text(content, first_lang)
    textB, confidenceB = speech_to_text(content, second_lang)
    return textA, first_lang if confidenceA > confidenceB else textB, second_lang

@app.route("/recorded", methods=['GET', 'POST'])
def recorded():
    if(request.form['CallStatus'] == 'completed':
        second_lang = ''
        return

    url = request.form['RecordingUrl']
    print(url)
    time.sleep(0.5)

    # get .wav file
    audio_file = urllib.request.urlopen(url)
    content = audio_file.read()

    response = VoiceResponse()
    if second_lang == '':
        text, _ = speech_to_text(content, first_lang)
        second_lang = findLang(text)
        # start recording for language
        response.say('Ready to translate.', voice='alice', language=first_lang)
        response.record(action='/recorded', timeout=twilio_timeout, trim='trim-silence')
        return str(response)
    else:
        text, lang = get_higher_confidence(content)
    print(text)

    target_lang = first_lang if lang == second_lang else second_lang
    translated_text = translate(text, lang, target_lang)
    print(translated_text)

    response.say(translated_text, voice='alice', language=target_lang)
    response.record(action='/recorded', timeout=twilio_timeout, trim='trim-silence')
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
