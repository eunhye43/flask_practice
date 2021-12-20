# -*- coding: utf-8 -*-
import sqlite3
from datetime import datetime

class Database:
        def __init__(self):
            self.conn = sqlite3.connect("database.db")
        # db 연결하고
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

        # def create_user_table(self):
        #     cur = self.conn.cursor()
        #     cur.execute("""
        #             create table user(
        #                 email text not null,
        #                 password text not null
        #                 );
        #                 """
        #             )
        #     self.conn.commit()

        def get_user(self):
            cur = self.conn.cursor()
            cur.execute("""
                    select * from user
                    """)
            rows = cur.fetchall()
            return rows
        # 데이터 삽입 insert (fetch안쓰고 commmit)
        def insert_question(self, subject, content):
            cur = self.conn.cursor()
            print(subject, content)
            cur.execute(
                '''
                INSERT INTO question (id, subject, content)
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

        def get_user(self):
            cur = self.conn.cursor()
            cur.execute("""
                    select * from user
                    """)
            rows = cur.fetchall()
            return rows

        def check_user_email(self, email):
            cur = self.conn.cursor()
            cur.execute("""
                select email from user where email = ?
                """, (email))
            row = cur.fetchone()
            return row
>>>>>>> f8faefeac2977d451953f360acf40c9f2e5440ed

        def SignUp(self, email, password):
            cur = self.conn.cursor()
            cur.execute(
                """
                INSERT INTO user (email, password)
                VALUES (?,?)
                """, (email, password))
            self.conn.commit()
            return {"message":"User_created_compeleted!"}

        def SignIn(self):
            cur = self.conn.cursor()
            cur.execute(
                """
                SELECT * FROM user WHERE user_id = %s AND user_pw = %s
                """)
            account = cur.fetchone()
            return {"result":account}

        def __del__(self):
            self.conn.close()