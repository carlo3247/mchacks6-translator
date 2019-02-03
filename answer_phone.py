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

twilio_timeout = 2
first_lang = 'en-US'
second_lang = ''

app = Flask(__name__)
stt_client = speech.SpeechClient()

def speech_to_text(audio_content, lang):
    # stt using google cloud
    audio = types.RecognitionAudio(content=audio_content)
    config = types.RecognitionConfig(language_code=lang)
    stt_response = stt_client.recognize(config, audio)
    text = ''
    confidence = 0
    if len(stt_response.results) > 0:
        text = stt_response.results[0].alternatives[0].transcript
        confidence = stt_response.results[0].alternatives[0].confidence
    return text, confidence

def get_higher_confidence(content):
    textA, confidenceA = speech_to_text(content, first_lang)
    textB, confidenceB = speech_to_text(content, second_lang)
    print('text: {} confidence: {} lang: {}'.format(textA, confidenceA, first_lang))
    print('text: {} confidence: {} lang: {}'.format(textB, confidenceB, first_lang))
    if confidenceA > confidenceB:
        return textA, first_lang
    else:
        return textB, second_lang

@app.route("/recorded", methods=['GET', 'POST'])
def recorded():
    global second_lang
    response = VoiceResponse()

    if request.form['CallStatus'] == 'completed':
        second_lang = ''
        response.hangup()
        return str(response)

    url = request.form['RecordingUrl']
    print(url)
    time.sleep(0.5)

    # get .wav file
    audio_file = urllib.request.urlopen(url)
    content = audio_file.read()

    if second_lang == '':
        text, _ = speech_to_text(content, first_lang)
        print(text)
        second_lang = langaugeIdentifier.findLang(text)
        print(second_lang)
        # start recording for language
        if second_lang == '':
            response.say('Please tell me your target language again.', voice='alice', language=first_lang)
        else:
            response.say('Ready to translate.', voice='alice', language=first_lang)
        response.record(action='/recorded', timeout=twilio_timeout, trim='trim-silence')
        return str(response)

    text, lang = get_higher_confidence(content)

    if text == '':
        response.say('Sorry, please repeat.', coive='alice', language=first_lang)
        response.record(action='/recorded', timeout=twilio_timeout, trim='trim-silence')
        return str(response)

    print('|{}|'.format(lang))
    print('detected {}'.format(lang))
    print('first {} second {}'.format(first_lang, second_lang))
    target_lang = first_lang if lang == second_lang else second_lang
    print('target {}'.format(target_lang))
    translated_text = watson.translate(text, lang, target_lang)
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
