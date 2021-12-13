import sqlite3

conn = sqlite3.connect("database.db")

cur = conn.cursor()

cur.execute("select * from question")

rows = cur.fetchall()
for row in rows:
    print(row)
    
conn.close()

# DB_PATH = "./database.db"

# class Database:
#     def __init__(self):
#         self.conn = sqlite3.connect(DB_PATH, isolation_level=None)
    # sqlite3 connection 연결

    # def get_posts(self, page=1):
    #     cur = self.conn.cursor()
        # connection으로부터 cur생성
        # cur.execute(
		# 	'''
		# 	SELECT * FROM post
		# 	ORDER BY updated_at DESC
		# 	LIMIT ?, ?
		# 	''', 
		# 	((page - 1) * 10, 10)
		# )
        # sql문 실행
    #     self.conn.close()
	# return cur.fetchall()
    # fetchall()은 모든 데이터를 한꺼번에 클라이언트로 가져올 때 사용
    # fetchone()은 한번 호출에 하나의 row만 가져올 때 사용
