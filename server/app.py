from flask import Flask, render_template
from twilio.rest import Client

app = Flask(__name__,template_folder='../client/templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/landing')
def landing():
    return render_template('landing.html')

@app.route('/form')
def form():
    return render_template('form.html')

client = Client(account_sid, auth_token)

def sendMessage(number,text):
    message = client.messages.create(
        to="+1" + number, #assume all numbers are US based
        from_="+14782495437", #automatic twilio number
        body=text)  
    # print(message.sid)

# sendMessage("2018381407","working")

