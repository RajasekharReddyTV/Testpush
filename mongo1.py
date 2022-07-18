import pymongo
client = pymongo.MongoClient("mongodb+srv://Rajasekhar:Gadwal123@cluster0.7uegq.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {"name": "Rajasekhar", "email":"raja@gmail.com","Surname": "Sekhar"}
d = {"name": "Rajasekhar", "email":"raja@gmail.com","Surname": "Sekhar"}
d = {"name": "Rajasekhar", "email":"raja@gmail.com","Surname": "Sekhar"}
d = {"name": "Rajasekhar", "email":"raja@gmail.com","Surname": "Sekhar"}
d = {"name": "Rajasekhar", "email":"raja@gmail.com","Surname": "Sekhar"}
d = {"name": "Rajasekhar", "email":"raja@gmail.com","Surname": "Sekhar"}
d = {"name": "Rajasekhar", "email":"raja@gmail.com","Surname": "Sekhar"}
d = {"name": "Rajasekhar", "email":"raja@gmail.com","Surname": "Sekhar"}
db1 = client["mongotest"]
coll = db1['test']
coll.insert_one(d)




