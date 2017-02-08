from pymongo import MongoClient
from csv import reader, DictReader

server = MongoClient('homer.stuy.edu')
db = server.CashMeOusside

def average(L):
    if len(L) != 0: 
        return sum(L) / len(L)
    else:
        return 0

peeps = [peep for peep in db.student.find()]

for peep in peeps:
    print peep['name'], peep['id'], average([int(course['mark']) for course in peep['grades']])
