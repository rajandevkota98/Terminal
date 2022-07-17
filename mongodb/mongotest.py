import pymongo
client = pymongo.MongoClient("mongodb+srv://Rajan:RAJAN123@cluster0.i2njg.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d ={

    "name":"Rajan",
    "email":"r.devkota.98@gmail.com"
}


db1= client['FSDS']
coll = db1['test1']
coll.insert_one(d)