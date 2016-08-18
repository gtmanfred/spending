import os
import socket

from flask import Flask
from .models import Receipts, db

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def hello():
    return "Hello World from {0}!".format(socket.gethostname())

if __name__ == '__main__':
    app.run('0.0.0.0')
