from flask import Flask
from twilio.rest import Client

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

# # Your Account SID from twilio.com/console
# account_sid = "AC094bc9651cf72d8d19434194b5f638b7"
# # Your Auth Token from twilio.com/console
# auth_token  = "3ee1da683abae91d2fee555033c331e3"

# client = Client(account_sid, auth_token)

# def sendMessage(number,text):
#     message = client.messages.create(
#         to="+1" + number, #assume all numbers are US based
#         from_="+14782495437", #automatic twilio number
#         body=text)  
#     # print(message.sid)

# sendMessage("2018381407","working")

