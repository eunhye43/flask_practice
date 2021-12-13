# -*- coding: utf-8 -*- 
import sqlite3
from datetime import datetime

class Database:
        def __init__(self):
            self.conn = sqlite3.connect("database.db")

        def SignUp(self):
            cur = self.conn.cursor()
            cur.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
            account = cur.fetchone()
            return 
            conn.close()