import pymongo

client = pymongo.MongoClient("mongodb+srv://premkgowda:nannamongodb@cluster0.bjiti.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "firstname": "prem",
    "email": "premkgowda@gmail.com",
    "lastname": "puttegowda",
}

db1 = client['mongotest']
coll = db1['test']

coll.insert_one(d)