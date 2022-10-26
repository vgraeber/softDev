#Clyde "Thluffy" Sinclair
#SoftDev  
#skeleton/stub :: SQLITE3 BASICS
#Oct 2022

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#only create if not exist already
command = "create table if not exists students(name text, age int, id text)"
c.execute(command)

command = "create table if not exists courses(code text, mark int, id text)"
c.execute(command)

#==========================================================


# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >

with open ('students.csv', newline ='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #print(row['name'], row['age'], row['id'])
        command = f"insert into students values('{row['name']}',{row['age']},{row['id']})" #only seems to work when the first {} in the fstr is in quotes
        c.execute(command)

with open ('courses.csv', newline ='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #print(row['code'], row['mark'], row['id'])
        command = f"insert into students values('{row['code']}',{row['mark']},{row['id']})"
        c.execute(command)

'''
command = "create table urmom(weight int, height int, age int, sexiness double)"          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

command = "insert into urmom values(1000,60,120,1000.0)"
c.execute(command)
'''

c.execute('select * from students;')

'''
print(c.fetchone())
print (c.fetchmany()) # these two lines will return the first element, and then the next two elements on another line.
'''


for i in c.fetchall(): # returns a list of strings
    print (i) #fetch retrieves the data, but because it fetches all of the data in the query, you can't run it twice for one query

print (c.fetchall()) # will return empty list here

#==========================================================

db.commit() #save changes
db.close()  #close database


