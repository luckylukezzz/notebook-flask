from flask import Blueprint , render_template
from . import mysql
views = Blueprint('views',__name__)   

@views.route('/')
def home():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT first_name FROM user")
    data = cursor.fetchall()
    cursor.close()
    return render_template('home.html', data=data)