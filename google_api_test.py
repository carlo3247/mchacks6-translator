import io
import os
import urllib.request

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# Instantiates a client
client = speech.SpeechClient()

def test(url):
    audio_file = urllib.request.urlopen(url)
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(language_code='en-US')
# config = types.RecognitionConfig(language_code='de-DE')
# config = types.RecognitionConfig(language_code='es-ES')
    response = client.recognize(config, audio)
    text = response.results[0].alternatives[0].transcript
    confidence = response.results[0].alternatives[0].confidence

    print(text)
    print(confidence)
    # for result in response.results:
        # print('Transcript: {}'.format(result.alternatives[0]))


url = 'https://api.twilio.com/2010-04-01/Accounts/ACb7b8ed23845adc7dd85ffb8054a1f495/Recordings/REa64690389ae22a4a3457cd3877acc4e3'
test(url)
