from pymongo import MongoClient

server = MongoClient('localhost')
db = server.CashMeOusside
c= db.students

l = c.find()
for person in l:
    try:
        print person['name']
    except:
        {}