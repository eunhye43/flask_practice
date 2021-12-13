# -*- coding: utf-8 -*- 
import sqlite3
from datetime import datetime

class Database:
        def __init__(self):
            self.conn = sqlite3.connect("database.db")

        # SQL query
        def get_question(self):
            cur = self.conn.cursor()
            cur.execute("select * from question")
            rows = cur.fetchall()
            for row in rows:
                print(rows)
            return rows
            conn.close()

        def get_answer(self):
            cur = self.conn.cursor()
            cur.execute("select * from answer")
            rows = cur.fetchall()
            for row in rows:
                print(rows)
            return rows
            conn.close()
        

        def insert_question(self, subject, content):
            cur = self.conn.cursor()
            cur.execute(
                "INSERT INTO question (subject, content) 
                VALUES (?,?)"
            )
            self.conn.commit()
            self.conn.close()
        
        def insert_answer(self, question_id, content):
            cur = self.conn.cursor()
            cur.execute(
                "INSERT INTO answer (question_id, content) 
                VALUES (?,?)"
            )
            self.conn.commit()
            self.conn.close()

        def __del__(self):
            self.conn.close()
        
# rows = cur.fetchall()
# for row in rows:
#     print(row)
    
# conn.close()

# DB_PATH = "./database.db"

# class Database:
#     def __init__(self):
#         self.conn = sqlite3.connect(DB_PATH, isolation_level=None)
#     # sqlite3 connection 연결

#     def get_question(self):
#         cur = self.conn.cursor()
#         # connection으로부터 cur생성
#         cur.execute(
# 			'''
# 			SELECT * FROM question
# 			ORDER BY id DESC
# 			'''
# 		)
#         # sql문 실행
#         # self.conn.close()
# 	    return cur.fetchall()

#     # fetchall()은 모든 데이터를 한꺼번에 클라이언트로 가져올 때 사용
#     # fetchone()은 한번 호출에 하나의 row만 가져올 때 사용

#     def insert_question(self, subject, content):
#         cur = self.conn.cursor()
#         now_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         cur.execute(
#             '''
#             insert into question(subject, content)
#             values('python', 'how to study python?')
#             ''',
#             (subject, content)
#         )
#         self.conn.commit()

#     def __del__(self):
# 		self.conn.close()