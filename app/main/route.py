from main import app,bcrypt
from flask import render_template, url_for, redirect, flash, request
from main.form import loginForm, RegisterForm
from main.model import User, db
from flask_login import login_user


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        flash(f'Check your uernsme or password {form.password.data}')
        
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            flash(f'You are now logged-in as {user.username}')
            login_user(user)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("home"))
    return render_template("login.html", form = form)


@app.route('/register', methods= ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        pas_hash =  bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username= form.username.data, email=form.email.data, password= pas_hash)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash(f'Your account have been  created as {form.username.data}!', category="success")
        return redirect(url_for('login'))
    return render_template("register.html", form = form)

@app.route('/voice')
def voice():
    return render_template("voice.html")