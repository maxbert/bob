from pymongo import MongoClient
import csv       #facilitates CSV I/O
server = MongoClient("149.89.150.100")
db = server['bob']
students = db['students']

fObj = open("peeps.csv") 
d1=csv.DictReader(fObj)

gObj = open("courses.csv")
d2=csv.DictReader(gObj)


for name in d1:

    globaldict = {}
    namer = d1[name]
    globaldict[name] = namer
    ider = d1[id]
    globaldict[id] = ider
    students.insert_one(globaldict) 
