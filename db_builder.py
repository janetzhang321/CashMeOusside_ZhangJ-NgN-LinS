#Sharon Lin, Nick Ng, Janet Zhang
#SoftDev2 pd6
#HW1 -- hey MON, GO and get some data!
#2017-02-06  

from pymongo import MongoClient

#server = MongoClient('149.89.150.100')

server = MongoClient('lisa.stuy.edu')

db = server.CashMeOusside
c = db.students


plist = []

f = open('peeps.csv').read().split('\n')[1:]

for line in f:
	if line == "":
		continue 
	pdict = {}
	pdict['name'] = line.split(',')[0]
	pdict['age'] = line.split(',')[1]
	pdict['id'] = line.split(',')[2]
	plist.append(pdict)
	
c.students.insert_many(plist)

clist = []

f = open('courses.csv').read().split('\n')[1:]

for line in f:
	if line == "":
		continue 
	cdict = {}
	cdict['code'] = line.split(',')[0]
	cdict['mark'] = line.split(',')[1]
	cdict['id'] = line.split(',')[2]
	clist.append(cdict)
	
c.students.insert_many(clist)


