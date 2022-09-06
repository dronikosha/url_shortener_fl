from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from environs import Env

env = Env()
env.read_env()

app = Flask(__name__,
            static_url_path='',
            static_folder='static',)
app.config['SECRET_KEY'] = env.str('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = env.str('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
domain = env.str('DOMAIN')

db = SQLAlchemy(app)


from url_shortner import models, routes
db.create_all()