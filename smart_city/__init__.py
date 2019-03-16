from config import Config
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy

smart_city = Flask(__name__)
smart_city.config.from_object(Config)
db = SQLAlchemy(smart_city)

from smart_city import routes