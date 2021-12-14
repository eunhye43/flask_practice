from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client.asd

collection = client.asd.asd2
result = collection.find() # select * from asd2
result = collection.find(
    {          
        'user_id':12,
        'status':9,
    },
# 9보다 높은 값? -> 'status':{'$gt':9},
    {
        'nickname':{'$in': ['asd', 'zxc']},
            }
    )

# python + mongodb = pymongo
# mongodb console (shell) : mongosh