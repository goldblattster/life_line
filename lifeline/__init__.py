from flask import Flask, session
import random
import string

app = Flask(__name__)

app.config["SECRET_KEY"] = "KeepThisS3cr3t"

def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(32))
    return session['_csrf_token']

app.jinja_env.globals['csrf_token'] = generate_csrf_token

import lifeline.views
import lifeline.helpers