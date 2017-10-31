"""
SendMe: Server
messages.py
version 0.1
desc: classes for the messages api calls
"""

from flask_restful import Resource, reqparse
import sqlite3
from datetime import datetime

class NewMessage(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('title', type=str, required=True, help="Title cannot be blank")
            parser.add_argument('content', type=str, required=True, help="Content cannot be blank")
            args = parser.parse_args()
            conn.execute("INSERT INTO messages (title, content, state, timestamp) VALUES (?, ?, ?, ?)", args['title'], args['content'], 0, datetime.now())
            return {"result":"SUCCESS"}
        except Exception as e:
            return {"result":e}

class UpdateMessage(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id', type=str, required=True, help="ID cannot be blank")
            parser.add_argument('state', type=str, required=True, help="Stage cannot be blank")
            args = parser.parse_args()
            conn.execute("UPDATE messages SET state=? WHERE id=?", args['state'], args['id'])
            return {"result":"SUCCESS"}
        except Exception as e:
            return {"result":e}

class GetMessages(Resource):
    def get(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('messages', type=str, required=True, help="Messages cannot be blank")
            args = parser.parse_args()
            query = conn.execute("SELECT * FROM messages ORDER BY ID DESC LIMIT 100 OFFSET ?", args['messages'])
            return {"messages": [dict(zip(tuple (query.keys()), i)) for i in query.cursor]}
        except Exception as e:
            return {"result":e}
