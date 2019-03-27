from flask import Flask, render_template, request
import requests
import pyotp
from tfa_secret import TFA_SECRET

app = Flask('myapp')
if not TFA_SECRET:
    raise ValueError('TFA_SECRET is not set')

MY_TOTP = pyotp.totp.TOTP(TFA_SECRET)
qr_url = MY_TOTP.provisioning_uri("alamakota@google.com", issuer_name="Secure App")

def check_credentials(code):
    return MY_TOTP.verify(code)

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        access = check_credentials(request.form['code'])
        return render_template('index.html', access=access, qr=qr_url)
    return render_template('index.html', qr=qr_url)
