from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from os import getenv

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI']=getenv('FLASK_BLOG_URI')
app.config['SECRET_KEY']=getenv('SECRET_KEY')
db = SQLAlchemy(app)




login_manager = LoginManager(app)
login_manager.login_view = 'login'


from application import routes
