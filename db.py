from pymongo import MongoClient
import csv     #facilitates CSV I/O
server = MongoClient("149.89.150.100")
db = server['bob']
students = db['students']

fObj = open("peeps.csv") 
d1=csv.DictReader(fObj)


for name in d1:
    gObj = open("courses.csv")
    d2=csv.DictReader(gObj)
    globaldict = {}
    namer = name['name']
    globaldict['name'] = namer
    ider = name['id']
    globaldict['id'] = ider
    ager = name['age']
    globaldict['age'] = ager
    for code in d2:
        #print name
        if (code['id'] == ider):
            key = code['code']
            globaldict[key] = code['mark']
    print globaldict
    students.insert_one(globaldict) 
             
