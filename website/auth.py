from flask import Blueprint,render_template,request ,redirect,url_for, flash
from . import mysql

auth = Blueprint('auth',__name__)   

@auth.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        cursor = mysql.connection.cursor()

        # Check if the email is registered
        cursor.execute("SELECT * FROM user WHERE email = %s", (email,))
        existing_user = cursor.fetchone()

        if not existing_user:
            flash('Theres no registered users in this email address. try again', category='error')
        else:
            if existing_user[2] != password :
                 flash('Incorrect password. try again',category='error')
            else:
                flash('Login success!',category='success')
                return redirect(url_for('auth.logout'))


    return render_template('login.html')


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up',methods=['POST','GET'])
def signUp():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash("Email must contain more than 3 chars" , category='error')
        elif len(firstName) < 2:
            flash("first name must contain more than 1 char" , category='error')
        elif len(password1) < 3:
            flash("password must contain more than 3 chars" , category='error')
        elif password1 != password2:
            flash("passwords dosen't match" , category='error')
        else: 
            cursor = mysql.connection.cursor()

             # Check if the email is already in use
            cursor.execute("SELECT * FROM user WHERE email = %s", (email,))
            existing_user = cursor.fetchone()

            if existing_user:
                flash('Email is already in use. Please choose a different one.', 'error')
            else:
                cursor.execute(
                    "INSERT INTO user (email, first_name, password) VALUES (%s, %s, %s)",
                    (email, firstName, password1)
                )
                mysql.connection.commit()
                cursor.close()
                flash("account creation successfull" , category='success')
                return redirect(url_for('auth.login'))
        
    return render_template('sign_up.html')
