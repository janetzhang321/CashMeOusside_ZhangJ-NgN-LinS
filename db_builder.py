
#Sharon Lin, Nick Ng, Janet Zhang
#SoftDev2 pd6
#HW1 -- hey MON, GO and get some data!
#2017-02-06  

from pymongo import MongoClient

#server = MongoClient('149.89.150.100')

server = MongoClient('homer.stuy.edu')

db = server.CashMeOusside
c = db.students

vals = {}

f = open('peeps.csv').read().split('\n')[1:]

for line in f:
	if line != "":
		doc = { 'id': line.split(',')[2], 'age': line.split(',')[1], 'name': line.split(',')[0], 'courses': ""}
		vals[line.split(',')[2]] = doc

f = open("courses.csv").read().split('\n')[1:]

for line in f:
	if line != "":
		doc = {line.split(',')[0]: line.split(',')[1]}
		if vals[line.split(',')[2]].get('courses'):
			vals[line.split(',')[2]]['courses'].update(doc)
		else:
			vals[line.split(',')[2]]['courses'] = doc

c.insert_many(vals.values())

print("Done")

#-----------------------------------------------------------------------

