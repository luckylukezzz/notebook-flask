from flask import Blueprint , render_template ,session,request,flash ,redirect,url_for
from . import mysql
views = Blueprint('views',__name__)   

@views.route('/home',methods=['POST','GET'])
def home():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id,data FROM note WHERE user_id = %s ORDER BY id DESC", (session['id'],))
    allnotes = cursor.fetchall()
    cursor.close()

    if request.method == 'POST':
        note = request.form.get('note')
        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO note (data, user_id) VALUES (%s, %s)",
            (note,session['id'])
                )
        mysql.connection.commit()
        cursor.close()
        flash("note added" , category='success')
        return redirect(url_for('views.home'))
    
    return render_template('home.html', first_name = session['first_name'] , allnotes = allnotes)