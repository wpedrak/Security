#!/usr/bin/env python3
from flask import Flask, url_for
from pathlib import Path

from flask_saml2.sp import ServiceProvider, create_blueprint
from flask_saml2.utils import certificate_from_file, private_key_from_file

KEY_DIR = Path(__file__).parent / 'keys'
IDP_CERTIFICATE_FILE = KEY_DIR / 'idp-certificate.pem'
IDP_CERTIFICATE = certificate_from_file(IDP_CERTIFICATE_FILE)

SP_CERTIFICATE_FILE = KEY_DIR / 'sp-kot-certificate.pem'
SP_PRIVATE_KEY_FILE = KEY_DIR / 'sp-kot-private-key.pem'
SP_CERTIFICATE = certificate_from_file(SP_CERTIFICATE_FILE)
SP_PRIVATE_KEY = private_key_from_file(SP_PRIVATE_KEY_FILE)

class ServiceProvider(ServiceProvider):
    def get_logout_return_url(self):
        return url_for('index', _external=True)

    def get_default_login_return_url(self):
        return url_for('index', _external=True)


sp = ServiceProvider()

app = Flask(__name__)
app.debug = True
app.secret_key = 'not a secret'

app.config['SERVER_NAME'] = 'www.kot.pl:9000'
app.config['SAML2_SP'] = {
    'issuer': 'Test SP',
    'certificate': SP_CERTIFICATE,
    'private_key': SP_PRIVATE_KEY,
}

IDP_URL = 'http://www.idp.pl:8000'

app.config['SAML2_IDENTITY_PROVIDERS'] = [
    {
        'CLASS': 'flask_saml2.sp.idphandler.IdPHandler',
        'OPTIONS': {
            'display_name': 'My security5 IDP',
            'entity_id': f'{IDP_URL}/saml/metadata.xml',
            'sso_url': f'{IDP_URL}/saml/login/',
            'slo_url': f'{IDP_URL}/saml/logout/',
            # 'entity_id': 'https://security5.eu.auth0.com/samlp/metadata/nEy9OgdToy6dMJCflnKj8h76B8ZILN1J',
            # 'sso_url': 'https://security5.eu.auth0.com/samlp/nEy9OgdToy6dMJCflnKj8h76B8ZILN1J',
            # 'slo_url': 'https://security5.eu.auth0.com/samlp/nEy9OgdToy6dMJCflnKj8h76B8ZILN1J',
            'certificate': IDP_CERTIFICATE,
        },
    },
]


@app.route('/')
def index():
    if sp.is_user_logged_in():
        auth_data = sp.get_auth_data_in_session()

        message = f'''
        <h3>Welcome to <strong>KOT</strong> service. Nice to meaw you.</h3>
        <p>You are logged in as <strong>{auth_data.nameid}</strong>.<p>
        '''


        logout_url = url_for('flask_saml2_sp.logout')
        logout = f'<form action="{logout_url}" method="POST"><input type="submit" value="Log out"></form>'

        return message + logout
    else:
        message = '''
        <h3>Welcome to <strong>KOT</strong> service. Nice to meaw you.</h3>
        <p>You are logged out.</p>
        '''

        login_url = url_for('flask_saml2_sp.login')
        link = f'<p><a href="{login_url}">Log in to continue</a></p>'

        return message + link


app.register_blueprint(create_blueprint(sp), url_prefix='/saml/')


if __name__ == '__main__':
    app.run(host='www.kot.pl', port=9000)
