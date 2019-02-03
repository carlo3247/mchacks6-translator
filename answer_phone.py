from flask import Flask
from flask import request
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/recorded", methods=['GET', 'POST'])
def recorded():
    print('url: {}'.format(request.form['RecordingUrl']))
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
