# -*- coding: utf-8 -*- 
import sqlite3
from datetime import datetime

class Database:
        def __init__(self):
            self.conn = sqlite3.connect("database.db")

        def SignIn(self):
            cur = self.conn.cursor()
            cur.execute(
                'SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
            account = cur.fetchone()
            return 
            conn.close()


        # 다보여주기 select (fetchall)
        def get_question(self):
            cur = self.conn.cursor() # cursor생성하고
            cur.execute("""
                select * from question
                """) # sql 쿼리 실행하고
            rows = cur.fetchall()
            return rows

        def get_answer(self):
            cur = self.conn.cursor()
            cur.execute("""
                    select * from answer
                    """)
            rows = cur.fetchall()
            return rows
        
        # 데이터 삽입 insert (fetch안쓰고 commmit)
        def insert_question(self, subject, content):
            cur = self.conn.cursor()
            print(subject, content)
            cur.execute(
                '''
                INSERT INTO question (subject, content)
                values (?,?)
                ''', (subject, content)
            )
            self.conn.commit()
        
        def insert_answer(self, question_id, content):
            cur = self.conn.cursor()
            cur.execute(
                '''
                INSERT INTO answer (question_id, content) 
                VALUES (?,?)
                ''', (question_id, content)
            )
            self.conn.commit()

        def __del__(self):
            self.conn.close()