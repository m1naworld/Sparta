from dotenv import load_dotenv
import os
from pymongo import MongoClient
import certifi

load_dotenv()
ID = os.environ['DB_ID']
PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
DB = os.getenv('PROJECT')

string = f"mongodb+srv://{ID}:{PASSWORD}@cluster0.gmnuoao.mongodb.net/{DB_NAME}?retryWrites=true&w=majority"
print(string)

client = MongoClient(string, tlsCAFile=certifi.where())
db = client.spart


# 저장 - 예시
# doc = {'name':'bobby','age':21}
# db.users.insert_one(doc)

# 한 개 찾기 - 예시
# user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
# all_users = list(db.users.find({},{'_id':False}))

# 바꾸기 - 예시
# db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
# db.users.delete_one({'name':'bobby'})