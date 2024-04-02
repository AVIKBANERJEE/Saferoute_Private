from flask import render_template,redirect,url_for,request,flash,Flask
from app import app
from app.auth import auth_signup,auth_login


@app.route('/',endpoint='index')
def home():
    return render_template("index.html")

@app.route('/login',methods=['POST'])
def login():
    email=request.form['email']
    pswd=request.form['password']
    if auth_login(email,pswd):
        flash("Logged in successfully","success")
        return render_template('index.html')
    else:
        flash("Invalid credentials","danger")
        return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    email = request.form['email']
    pswd = request.form['password']

    if auth_signup(email, pswd):
        flash("Account created successfully","success")
        return render_template('index.html')
    else:
        flash("An account already exists with this email","danger")
        return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/map')
def map():
    return render_template('map.html')

