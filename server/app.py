from flask import Flask
from twilio.rest import Client

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

client = Client(account_sid, auth_token)

def sendMessage(number,text):
    message = client.messages.create(
        to="+1" + number, #assume all numbers are US based
        from_="+14782495437", #automatic twilio number
        body=text)  
    # print(message.sid)

sendMessage("2018381407","working")

