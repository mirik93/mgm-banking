from mgmbanking import app, db
from flask import render_template, request, flash, redirect, url_for


# import of forms
from mgmbanking.forms import SignUpForm, LoginForm

#import models
from mgmbanking.models import User, check_password_hash, Post

#import flask login module/functions
from flask_login import login_user, current_user, logout_user

# Home Route
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/contact")
def creditcard():
    return render_template("contact.html")

@app.route("/register",methods=["GET","POST"])
def createUser():
    form = SignUpForm()
    if request.method == 'POST' and  form.validate():
        flash("Thanks for Signing up!")
        username = form.username.data
        email = form.email.data
        password = form.password.data
        print(username,email,password)

        #add form data to user model class
        user = User(username,email,password)
        db.session.add(user) #start comms with database
        db.session.commit() #save data to database
        return redirect(url_for('login'))

    else:
        print("Not valid")
    return render_template('register.html',register_form=form)

@app.route("/login",methods=["GET","POST"])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate():
        user_email = form.email.data
        password = form.password.data
        logged_user = User.query.filter(User.email == user_email).first
        if logged_user and check_password_hash(logged_user.password,password):
            login_user(logged_user)
            print(current_user.username)
            return redirect(url_for('home'))
    return render_template('login.html', form=form)

        