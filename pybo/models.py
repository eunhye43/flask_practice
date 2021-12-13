# import sqlite3
# from datetime import datetime

# DB_PATH = "./data.db"

# # 앞으로 모델을 추가하거나 변경할 때는 flask db migrate 명령이나 flask db upgrade 명령만 사용할 것이다. 
# # 즉, 앞으로 데이터베이스 관리를 위해 여러분이 기억해야 할 명령어는 이 2가지뿐이다.

# class Database:
#     def __init__(self):
#         self.conn = sqlite3.connect(DB_PATH, isolation_level=None)
    
#     def get_posts(self, page=1):
#         cur = self.conn.cursor()
#         cur.execute(
#             '''
#             select * from post
#             order by updated_at DESC
#             limit ?, ?
#             ''',
#             ((page - 1)) * 10, 10)
#         return cur.fetchall()

#     def insert_posts(self, name, title, content):
#         cur = self.conn.cursor()
#         now_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         cur.execute(
#             '''
#             insert into post (name, title, content, updated_at)
#             values('eunhye', 'flask', 'Easy to learn Flask', '2021-12-12 15:33:33')
#             '''
#             values('eunhye', 'flask', 'Easy to learn Flask', '2021-12-12 15:33:33')
#         )
#         self.conn.commit()
    
#     def __del__(self):
#         self.conn.close()

    
# def initialize_db():
#     conn = sqlite3.connect(DB_PATH, isolation_level=None)
#     cur = conn.cursor()
#     cur.execute('''
#             create table if not ixists post
#             (
#                 id integer primary key autoincrement,
#                 name text,
#                 title text,
#                 content text,
#                 updated_at text
#             )
#         ''')
#     conn.close()