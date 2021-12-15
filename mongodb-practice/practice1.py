from pymongo import MongoClient # pymongo 라이브러리 가져와줭
from datetime import datetime
from bson.objectid import ObjectId
from datetime import datetime

client = MongoClient("mongodb://localhost:27017") # 호스트에서 쓰고 있는 mongodb에 접속해줭 

db = client.pera #mango라고 하는 db를 생성해줘
fla = db.flask #그 db에 customer라는 테이블 만들거야
# 변수에 넣어줄 때는 {} 딕셔너리, 그리고 리스트로 감싸기
user_profiles = [
    
    {"user_id": 211, "name": "Luke"},
    {"user_id": 212, "name": "Ziltoid"}
    
]
result = db.flask.insert_many(user_profiles)
new_profile = {"user_id": 213, "name": "Drew"}
duplicate_profile = {"user_id": 212, "name": "Tommy"}

result = db.flask.insert_one(new_profile)
for doc in db.flask.find():
    print(doc)
# f = col.insertOne(b)
# c = col.insert_many(a)
# print(c) # table.insert_many(값)
#print(col.find({"sex":"Y"}, {"age": {"$gt":21}})) # col에 있는 값 다 찾기
# print(db.list_collection_names())
# db.table.insert_many()
# db.table.find({})

# new_posts = [
#     {
#      "author": "Mike",
#      "text": "Another post!",
#      "tags": ["bulk", "insert"],
#      "age" : 22
#     },
     
#     {
#      "author": "Eliot",
#      "title": "MongoDB is fun",
#      "text": "and pretty easy too!",
#      "age" : 20
#     },

#     {
#      "author": "Mike",
#      "title": "Flask is Fa",
#      "text": "How to learn Flask!",
#      "age" : 22
#     }
    
# ]


# result = hi.insert_many(new_posts)
# # print(result.inserted_ids)
# print(result.inserted_ids)
# print(hi.count_documents({}))
# for i in hi.find({"age" : {"$gt":21}}).sort("author"):
#     print(i)
# print("@")
# print(c)
# print(d)
# print(col.find({"user_id":2}))
# print(col.find({"user_id":1}))

# user_profiles = [
#     {"user_id":211, "name" : "JJU"},
#     {"user_id":212, "name" : "AJI"}
# ]

# result = db.profiles.insert_many(user_profiles)


# find
# result1 = col.find() # select * from asd2 와 같다고 보면됨
# result2 = col.find( # 조건 두개 넣어줄 때는 요렇게
#     {          
#         'user_id':12,
#         'status':9,
#     },
# 9보다 높은 값? -> 'status':{'$gt':9}, '$'를 사용해주면됨
    # {
    #     'nickname':{'$in': ['asd', 'zxc']},
    #         }
    # )

# python + mongodb = pymongo
# mongodb console (shell) : mongosh

# insert

# my_dicts = [{"name":"BOBO", "address":"mapogu, Seoul", "date": datetime(2021, 12, 15, 10, 14)},
#            {"name":"mimi", "address":"sinchon, Seoul", "date": datetime(2021, 12, 15, 10, 14)},
#            {"name":"eunji", "address":"hasidong, Goyangsi", "date": datetime(2021, 12, 15, 10, 14)},
#            {"name":"kong", "address":"seogyodong, Goyangsi", "date": datetime(2021, 12, 15, 10, 14)},
#            {"name":"mimi", "address":"sinchon, Seoul", "date": datetime(2021, 12, 15, 10, 14)},
#            {"name":"mingki", "address":"gangnam, Seoul", "date": datetime(2021, 12, 15, 10, 14)}]

# col.count_documents({})
# print(col.count_documents({"name":"mimi"}))

# list = col.find().sort("name", -1)
# my_query = {"name":{"$regex":"^A"}}
# my_doc = col.find(my_query)

# a = db.list_collection_names() # 컬렉션 이름 쫙 보여줌
# print(a)

# ppint는 단일 자료만 뽑음
# pprint.pprint(col.find_one({"address":"Seoul"}))


# insert
# user_profiles = [
#     {"user_id":211, "name" : "JJU"},
#     {"user_id":212, "name" : "AJI"}
# ]

# result = db.profiles.insert_many(user_profiles)

# new_profile = {"user_id":213, "name": "Drew"}
# result = db.profiles.insert_one(new_profile)

# for doc in db.profiles.find():
#     pprint.pprint(doc)
#     print("____________")
#     print(doc)
#     print("____________")
