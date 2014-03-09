from lifeline import app, models
from flask import session
import hashlib

@app.context_processor
def inject_user():
    if 'user' in session:
        user_id = session['user']
        return dict(user=models.User.objects(id=user_id)[0])

    return dict(user="guest")

@app.context_processor
def user_gravatar():
    if 'user' in session:
        return dict(user_gravatar='http://www.gravatar.com/avatar/{0}'.format(hashlib.md5(bytes(models.User.objects(id=session['user'])[0].email, 'utf-8')).hexdigest()))
    else:
        return dict(user_gravatar='http://www.gravatar.com/avatar/5d838d342980740afbdc08e2ab17162d')