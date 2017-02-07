from pymongo import MongoClient
import csv     #facilitates CSV I/O
server = MongoClient("149.89.150.100")
db = server['bob2']
students = db['students']

fObj = open("peeps.csv") 
d1=csv.DictReader(fObj)

def dbinit():
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

def avg(dict d):
    avg = 0
    count = 0 
    if 'systems' in d.keys():
        avg += d['systems']
        count += 1
    if 'greatbooks' in d.keys():
        avg += d['systems']
        count += 1
        
    if 'ceramics' in d.keys():
        avg += d['systems']
        count += 1
    if 'softdev' in d.keys():
        avg += d['systems']
        count += 1
    return (avg / count)

def getavgs():
    p = s.bob2.students.find()
    for d in p:
        print avg(d)
