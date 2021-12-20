# -*- coding: utf-8 -*- 
import sqlite3
from datetime import datetime

class Database:
        def __init__(self):
            self.conn = sqlite3.connect("database.db")

        def SignIn(self):
            cur = self.conn.cursor()
            cur.execute(
                """
                SELECT * FROM accounts WHERE user_id = %s AND user_pw = %s
                """)
            account = cur.fetchone()
            return {"result":account}

        
        # 데이터 삽입 insert (fetch안쓰고 commmit)
        # def insert_question(self, subject, content):
        #     cur = self.conn.cursor()
        #     print(subject, content)
        #     cur.execute(
        #         '''
        #         INSERT INTO question (subject, content)
        #         values (?,?)
        #         ''', (subject, content)
        #     )
        #     self.conn.commit()
        
        # def insert_answer(self, question_id, content):
        #     cur = self.conn.cursor()
        #     cur.execute(
        #         '''
        #         INSERT INTO answer (question_id, content) 
        #         VALUES (?,?)
        #         ''', (question_id, content)
        #     )
        #     self.conn.commit()

        def __del__(self):
            self.conn.close()