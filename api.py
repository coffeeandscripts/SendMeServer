"""
SendMe: Server
api.py
version 0.1
desc: runs the main SendMe server with relevant api calls
"""

from flask import Flask, request
from flask_restful import Api
import sqlite3
from messages import *
from database import *

conn = start_database()
setup_database(conn)

app = Flask(__name__, static_folder='static', static_url_path='')
api = Api(app)

# post new message
api.add_resource(NewMessage, '/api/v1/new_message')
# post message state change
api.add_resource(UpdateMessage, '/api/v1/update_message')
# get all messages (last 100)
api.add_resource(GetMessages, '/api/v1/messages')

if __name__ == '__main__':
    app.run()
