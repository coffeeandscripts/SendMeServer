"""
SendMe: Server
database.py
version 0.1
desc: database setup and manipulation
"""

import sqlite3

def start_database():
    return sqlite3.connect('SendMe.sqlite3')

def setup_database(conn):
    conn.execute("CREATE TABLE if not EXISTS messages (id INTEGER PRIMARY KEY AUTOINCREMENT, title text, content text, state integer, [timestamp] timestamp)")
