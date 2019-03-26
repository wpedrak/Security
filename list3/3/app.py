from flask import Flask, render_template, request
import requests
from  recapcha_secrets import RECAPCHA_SECRET

app = Flask('myapp')
RECAPCHA_VERIFY_URL='https://www.google.com/recaptcha/api/siteverify'
if not RECAPCHA_SECRET:
    raise ValueError('RECAPCHA_SECRET is not set')

def check_capcha(user_response):
    print(f'user response: {user_response}')
    r = requests.post(
        RECAPCHA_VERIFY_URL,
        data={
            'secret': RECAPCHA_SECRET, 
            'response': user_response
        })
    print(r.status_code, r.reason)
    print(r.text)
    if r.status_code == 200:
        return r.json()['success']
    return False

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        capcha_result = check_capcha(request.form['g-recaptcha-response'])
        return render_template('index.html', human=capcha_result)
    return render_template('index.html')
