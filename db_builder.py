#Sharon Lin, Nick Ng, Janet Zhang
#SoftDev2 pd6
#HW1 -- hey MON, GO and get some data!
#2017-02-06  

from pymongo import MongoClient
from csv import reader, DictReader

#server = MongoClient('149.89.150.100')

courses = [course for course in DictReader(open('courses.csv'))]
peeps = [peep for peep in DictReader(open('peeps.csv'))]
teachers = [teacher for teacher in DictReader(open('teachers.csv'))]

server = MongoClient()
db = server.CashMeOusside

vals = [[] for i in range(len(peeps))]

for course in courses:
    studentID = int(course.pop('id')) - 1
    vals[studentID].append(course)

for i in range(len(peeps)):
    peeps[i]['grades'] = vals[i]
    db.students.insert_one(peeps[i])

for teacher in teachers:
    teacher['students'] = []
    for peep in peeps:
        if (teacher['code'] in [course['code'] for course in peep['grades']]):
            teacher['students'].append(peep['id'])
    db.teachers.insert_one(teacher)

print("Done")



