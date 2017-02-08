from pymongo import MongoClient
from csv import reader, DictReader

server = MongoClient()
db = server.CashMeOusside

def average(L):
    if len(L) != 0: 
        return sum(L) / len(L)
    else:
        return 0

print("Name, ID, Average")    
    
peeps = [peep for peep in db.students.find()]
peeps = peeps[0:len(peeps)/2]

for peep in peeps:
    print peep['name'], peep['id'], average([int(course['mark']) for course in peep['grades']])

print("Done")
