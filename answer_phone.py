from flask import Flask
from flask import request
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/test", methods=['GET', 'POST'])
def answer_call():
    resp = VoiceResponse()
    resp.say("We are all homos. Homo sapiens.", voice='alice')
    return str(resp)

@app.route("/recording", methods=['GET', 'POST'])
def test():
    print('in test')
    print('---')
    print('url: {}'.format(request.form['RecordingUrl']))
    print('---')
    response = VoiceResponse()
    response.hangup()

    return str(response)


@app.route("/answer", methods=['GET', 'POST'])
def record():
    response = VoiceResponse()
    response.say('Hello, Please leave a message after the beep.')
    print('recording...')
    response.record(action='/recording', timeout=3, trim='trim-silence')
    response.hangup()

    return str(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80,debug=True)
