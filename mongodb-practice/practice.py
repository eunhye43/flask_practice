from pymongo import MongoClient # pymongo 라이브러리 가져와줭
client = MongoClient("mongodb://localhost:27017") # 호스트에서 쓰고 있는 mongodb에 접속해줭 
db = client.asd #asd라고 하는 db를 생성해줘

collection = db.asd2 #asd2라는 테이블 만들거야
result = collection.find() # select * from asd2 와 같다고 보면됨
result = collection.find( # 조건 두개 넣어줄 때는 요렇게
    {          
        'user_id':12,
        'status':9,
    },
# 9보다 높은 값? -> 'status':{'$gt':9}, '$'를 사용해주면됨
    {
        'nickname':{'$in': ['asd', 'zxc']},
            }
    )

# python + mongodb = pymongo
# mongodb console (shell) : mongosh