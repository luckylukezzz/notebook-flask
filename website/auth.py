from flask import Blueprint,render_template,request , flash

auth = Blueprint('auth',__name__)   

@auth.route('/login', methods=['POST','GET'])
def login():
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
        if len(firstName) < 2:
            flash("first name must contain more than 1 char" , category='error')
        if len(password1) < 7:
            flash("password must contain more than 7 chars" , category='error')
        if password1 == password2:
            flash("account creation successfull" , category='success')
        else:
            flash("passwords dosen't match" , category='error')
            
            


    return render_template('sign_up.html')
