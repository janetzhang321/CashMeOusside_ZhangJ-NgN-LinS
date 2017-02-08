
from pymongo import MongoClient

server = MongoClient('homer.stuy.edu')
db = server.CashMeOusside


d = db.teachers
c= db.students

vals = {}
counter = 0

f = open('teachers.csv').read().split('\n')[1:]

for line in f:
    if line != "":
        m = c.find({'courses': {'name': line.split(',')[0] }})
        for person in m:
            print("--------------------")        
            print person
            print("--------------------")
        doc = {'name': line.split(',')[1], 'class': line.split(',')[0], 'period':line.split(',')[2], 'students':""}
        vals[counter] = doc
        counter += 1

    
#------------------------------------------------------------------


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
        print person
        print '\n'
    except:
        {}


