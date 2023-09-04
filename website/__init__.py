from flask import Flask ,session
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['SECRET_KEY'] = "asdfg"
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] ='2001'
app.config['MYSQL_DB'] = 'flasknoteapp'

mysql =MySQL(app)


from .views import views
from .auth import auth

app.register_blueprint(views, url_prefix='/') 
app.register_blueprint(auth, url_prefix='/') 
