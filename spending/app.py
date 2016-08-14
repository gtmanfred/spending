import os
import socket

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from .models import Receipts


@app.route('/')
def hello():
    return "Hello World from {0}!".format(socket.gethostname())

if __name__ == '__main__':
    app.run('0.0.0.0')
