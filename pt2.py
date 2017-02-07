
from pymongo import MongoClient

server = MongoClient('homer.stuy.edu')
db = server.CashMeOusside
c= db.students
l = c.find()


for person in l:#prints the names
    try:
        print person['name']
        grades = person['courses'].values()
        a=[]
        for item in grades:
            a.append(int(item))
        l=0
        for score in a:
            l += score
        pavg = float(l)/len(a)
        print pavg
        print person['id']
        print '\n'
    except:
        {}



