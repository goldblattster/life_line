from lifeline import app, models
from flask import render_template, request, session, abort, redirect, url_for
from datetime import date
from passlib.hash import sha256_crypt

@app.route('/')
def hello():
    return render_template('home.html')

@app.before_request
def csrf_protect():
    if request.method == "POST":
        token = session.pop('_csrf_token', None)
        if not token or token != request.form.get('_csrf_token'):
            abort(403)

@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        new_user = models.User(email=request.form['email'])
        new_user.name = request.form['name']
        new_user.password = sha256_crypt.encrypt(request.form['password'])
        new_user.birthdate = date(int(request.form['year']), int(request.form['day']), int(request.form['month']))
        new_user.gender = request.form['gender']

        if 'smoker' in request.form: # ariel this shit doesnt work
            new_user.smoker = True
        else:
            new_user.smoker = False

        new_user.save()
        return render_template('home.html', alert_info=['You have been registered. You may now sign in using your account.'])
    else:
        return render_template('register.html', current_year=date.today().year)

@app.route('/sign_in/', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        user = models.User.objects(email=request.form['email'])
        if len(user) < 1:
            return "Account doesn't exist"
        else:
            if sha256_crypt.verify(request.form['password'], user[0].password):
                session['user'] = str(user[0].id)
                return render_template('home.html', alert_info=['You are now signed in.'])
    else:
        return render_template('sign_in.html')

@app.route('/timeline')
def timeline():
    return render_template("timeline.html")

@app.route('/sign_out/')
def sign_out():
    session.pop('user', None)
    return redirect(url_for('hello'))
