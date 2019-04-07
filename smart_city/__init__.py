from config import Config
from flask import Flask, url_for
from flask_socketio import SocketIO, emit

smart_city = Flask(__name__)
smart_city.config.from_object(Config)

from smart_city import routes