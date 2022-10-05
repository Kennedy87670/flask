from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config["SECRET_KEY"] = '92d51cf8a4c01edec707ac81'
db = SQLAlchemy(app)

from market import routes 