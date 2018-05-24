from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[A-Z])(?=.*[0-9])')
NAME_REGEX = re.compile(r'^(?=.*[0-9])')
app = Flask(__name__)
app.secret_key = "CodingDojo"

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/process', methods=["POST"])

def process():
    errors = False
    email = request.form["email"]
    if len(email) < 1:
        errors = True
        flash("Email cannot be blank")
    elif not EMAIL_REGEX.match(email):
        errors = True
        flash("Please enter a valid email")

    fname = request.form["fname"]
    if len(fname) < 1:
        errors = True
        flash("First name cannot be blank")
    elif NAME_REGEX.match(fname):
        errors = True
        flash("First name must not contain any numbers")
    
    lname = request.form["lname"]
    if len(lname) < 1:
        errors = True
        flash("Last name cannot be blank")
    elif NAME_REGEX.match(lname):
        errors = True
        flash("Last name must not contain any numbers")

    password = request.form["password"]
    print(PASSWORD_REGEX.match(password))
    if len(password) < 9:
        errors = True
        flash("Password must be longer than 8 characters")
    elif not PASSWORD_REGEX.match(password):
        errors = True
        flash("Password must contain at least one upper case letter and at least one number.")

    confirm = request.form["confirm"]
    if confirm != password or len(confirm) < 1:
        errors = True
        flash("Passwords must match")

    if not errors:
        flash("Success!")
    return redirect('/')

app.run(debug=True)