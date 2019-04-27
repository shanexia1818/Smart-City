import firebase_admin
from config import Config
from firebase_admin import db
from flask import Flask, url_for
from firebase_admin import credentials, db

smart_city = Flask(__name__)
smart_city.config.from_object(Config)

# Intialise firebase 
# cred = credentials.Certificate("./smart_city_database_secret.json")

# firebase_admin.initialize_app(cred, options={
#     "databaseURL": "https://smart-city-61e3d.firebaseio.com"
# })

from smart_city import routes