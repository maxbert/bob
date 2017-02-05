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
    namer = name['name']
    globaldict['name'] = namer
    ider = name['id']
    globaldict['id'] = ider
    ager = name['age']
    globaldict['age'] = ager
    for code in d2:
        if code['id'] == name['id']
            globaldict[d2['code']] = d2['mark']
    students.insert_one(globaldict) 
             
