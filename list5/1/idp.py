#!/usr/bin/env python3
import logging
from pathlib import Path

from flask import Flask, abort, redirect, request, session, url_for
from flask.views import MethodView

from flask_saml2.idp import create_blueprint, idp
from flask_saml2.utils import certificate_from_file, private_key_from_file
from user import User

KEY_DIR = Path(__file__).parent / 'keys'
SP_KOT_CERTIFICATE_FILE = KEY_DIR / 'sp-kot-certificate.pem'
SP_KOT_CERTIFICATE = certificate_from_file(SP_KOT_CERTIFICATE_FILE)

SP_KOGUCIK_CERTIFICATE_FILE = KEY_DIR / 'sp-kogucik-certificate.pem'
SP_KOGUCIK_CERTIFICATE = certificate_from_file(SP_KOGUCIK_CERTIFICATE_FILE)

IDP_CERTIFICATE_FILE = KEY_DIR / 'idp-certificate.pem'
IDP_PRIVATE_KEY_FILE = KEY_DIR / 'idp-private-key.pem'
IDP_CERTIFICATE = certificate_from_file(IDP_CERTIFICATE_FILE)
IDP_PRIVATE_KEY = private_key_from_file(IDP_PRIVATE_KEY_FILE)


logger = logging.getLogger(__name__)
logging.basicConfig()

class IdentityProvider(idp.IdentityProvider):
    def login_required(self):
        if not self.is_user_logged_in():
            next = url_for('login', next=request.url)

            abort(redirect(next))

    def is_user_logged_in(self):
        return 'user' in session and session['user'] in users

    def logout(self):
        del session['user']

    def get_current_user(self):
        return users[session['user']]


users = {user.username: user for user in [
    User('ala', 'ala@gmail.com'),
    User('kot', 'kot@gmail.com'),
]}


idp = IdentityProvider()


class Login(MethodView):
    def get(self):
        options = ''.join(f'<option value="{user.username}">{user.email}</option>'
                          for user in users.values())
        select = f'<div><label>Select a user: <select name="user">{options}</select></label></div>'

        next_url = request.args.get('next')
        next = f'<input type="hidden" name="next" value="{next_url}">'

        submit = '<div><input type="submit" value="Login"></div>'

        form = f'<form action="." method="post">{select}{next}{submit}</form>'
        header = '<title>Login</title><p>Please log in to continue.</p>'

        return header + form

    def post(self):
        user = request.form['user']
        next = request.form['next']

        session['user'] = user
        print("Logged user", user, "in")
        print("Redirecting to", next)
        logging.info("Logged user", user, "in")
        logging.info("Redirecting to", next)

        return redirect(next)


app = Flask(__name__)
app.debug = True
app.secret_key = 'not a secret'
app.config['SERVER_NAME'] = 'www.idp.pl:8000'
app.config['SAML2_IDP'] = {
    'autosubmit': True,
    'certificate': IDP_CERTIFICATE,
    'private_key': IDP_PRIVATE_KEY,
}
app.config['SAML2_SERVICE_PROVIDERS'] = [
    {
        'CLASS': 'flask_saml2.idp.sp.demo.AttributeSPHandler',
        'OPTIONS': {
            'display_name': 'Kot Service Provider',
            'entity_id': 'http://www.kot.pl:9000/saml/metadata.xml',
            'acs_url': 'http://www.kot.pl:9000/saml/acs/',
            'certificate': SP_KOT_CERTIFICATE,
        },
    },
    {
        'CLASS': 'flask_saml2.idp.sp.demo.AttributeSPHandler',
        'OPTIONS': {
            'display_name': 'Kogucik Service Provider',
            'entity_id': 'http://www.kogucik.pl:9001/saml/metadata.xml',
            'acs_url': 'http://www.kogucik.pl:9001/saml/acs/',
            'certificate': SP_KOGUCIK_CERTIFICATE,
        },
    }
]

app.add_url_rule('/login/', view_func=Login.as_view('login'))
app.register_blueprint(create_blueprint(idp), url_prefix='/saml/')


if __name__ == '__main__':
    app.run(host='www.idp.pl', port=8000)
