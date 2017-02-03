from pymongo import MongoClient

server = MongoClient('149.89.150.100')
db = server.CashMeOusside
c = db.students

f = open('peeps.csv', 'r')
r = f.readlines()
for line in r:
	c.students.insert_one({line.split()
