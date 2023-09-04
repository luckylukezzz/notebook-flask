from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_mysqldb import MySQL

# db = SQLAlchemy()
# DB_NAME = "database.db"

# def create_app():
app = Flask(__name__)
app.config['SECRET_KEY'] = "asdfg"
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] ='2001'
app.config['MYSQL_DB'] = 'flasknoteapp'
# app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
# db.init_app(app)
mysql =MySQL(app)

from .views import views
from .auth import auth

app.register_blueprint(views, url_prefix='/') 
app.register_blueprint(auth, url_prefix='/') 

# from .models import User, Note
# create_database(app)

    # return app

# def create_database(app):
#     if not path.exists('website/' + DB_NAME):
#         db.create_all()
#         print('Created Database!')
