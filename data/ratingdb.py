import sqlite3
import csv
import pandas as pd


conn=sqlite3.connect('film.db')
cursor=conn.cursor()

cursor.execute("""
DROP TABLE IF EXISTS ratings
""")
cursor.execute("""
DROP TABLE IF EXISTS basics
""")
cursor.execute("""
DROP TABLE IF EXISTS principals
""")
cursor.execute("""
DROP TABLE IF EXISTS name
""")

cursor.execute("""
DROP TABLE IF EXISTS nameCompll
""")
conn.commit()



cursor.execute("""
CREATE TABLE IF NOT EXISTS ratings(
       id TEXT PRIMARY KEY UNIQUE,
       average FLOAT,
       vote INTEGER
  )
  """)



cursor.execute("""
CREATE TABLE IF NOT EXISTS basics(
       id TEXT PRIMARY KEY UNIQUE,
       type TEXT,
       titre TEXT,
       date INTEGER,
       duration INTEGER,
       genres TEXT
  )
  """)



cursor.execute("""
CREATE TABLE IF NOT EXISTS principals(
       number INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
       id TEXT,
       ordering INTEGER,
       idPerson TEXT,
       job TEXT
  )
  """)




cursor.execute("""
CREATE TABLE IF NOT EXISTS name(
       number INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
       idPerson TEXT,
       name TEXT
  )
  """)

cursor.execute("""
CREATE TABLE IF NOT EXISTS nameCompll(
       idPerson TEXT PRIMARY KEY UNIQUE ,
       name TEXT
  )
  """)


#la fonction va couper la bdd et ne garder que les films avec plus de n votes
def ratingdb(n):
    with open('title.ratings.tsv') as tsvfile:
      reader = csv.reader(tsvfile, delimiter='\t')
      next(reader)#saute le header
      i=0
      for row in reader:
        if int(row[2])>=n:
          i=i+1
          addRating(row[0],row[1],row[2])
    return i

def basicdb():

  with open('title.basics.tsv') as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')
    cursor.execute("""SELECT id FROM ratings""")
    rows = cursor.fetchall()
    i=0
    for row in rows:
      for film in reader:
        if row[0]==film[0]:
          addBasic(film[0],film[1],film[2],film[5],film[7],film[8])
          break;
    return i

def principalsdb():
    with open('title.principals.tsv') as tsvfile:
      reader = csv.reader(tsvfile, delimiter='\t')
      cursor.execute("""SELECT id FROM ratings""")
      rows = cursor.fetchall()
      for row in rows:
        for person in reader:
          if row[0]==person[0]:
            #print(person[0],person[1],person[2],person[3])
            addPrincipal(person[0],person[1],person[2],person[3])
            if person[1]=='9':
              break;
'''
def namedb():
    with open('name.basics.tsv') as tsvfile:
      reader = csv.reader(tsvfile, delimiter='\t')
      cursor.execute("""SELECT idPerson FROM principals""")
      rows = cursor.fetchall()
      for row in rows:
        for person in reader:
          if row[0]==person[0]:
            print(person)
            break
'''
def namedb():
    cursor.execute("""SELECT idPerson FROM principals""")
    rows = cursor.fetchall()
    for row in rows:
      cursor.execute("""SELECT idPerson,name FROM nameCompll where idPerson=?""",(row[0],))
      person = cursor.fetchall()
      addName(person[0][0],person[0][1])
      #print(person[0][1])


def nameCompldb():
    with open('name.basics.tsv') as tsvfile:
      reader = csv.reader(tsvfile, delimiter='\t')
      for person in reader:
        cursor.execute("""INSERT INTO nameCompll(idPerson,name) VALUES(?,?)""",(person[0],person[1]))





def addRating(id,average,vote):
  cursor.execute("""INSERT INTO ratings(id,average,vote) VALUES(?,?,?)""",(id,average,vote))


def addBasic(id,type,titre,date,duration,genres):
  cursor.execute("""INSERT INTO basics(id,type,titre,date,duration,genres) VALUES(?,?,?,?,?,?)""",(id,type,titre,date,duration,genres))

def addPrincipal(id,ordering,idPerson,job):
  cursor.execute("""INSERT INTO principals(id,ordering,idPerson,job) VALUES(?,?,?,?)""",(id,ordering,idPerson,job))

def addName(idPerson,name):
  cursor.execute("""INSERT INTO name(idPerson,name) VALUES(?,?)""",(idPerson,name))






def readRating():
  cursor.execute("""SELECT id,average,vote FROM ratings""")
  rows = cursor.fetchall()
  for row in rows:
    print('{0} : {1} : {2}'.format(row[0], row[1], row[2]))


def readBasics():
  cursor.execute("""SELECT id,type,titre,date,duration,genres FROM basics""")
  rows = cursor.fetchall()
  for row in rows:
    print('{0} : {1} : {2} : {3} : {4} : {5}'.format(row[0], row[1], row[2],row[3], row[4], row[5]))

def readPrincipals():
  cursor.execute("""SELECT id,ordering,idPerson,job FROM principals""")
  rows = cursor.fetchall()
  for row in rows:
    print('{0} : {1} : {2} : {3}'.format(row[0], row[1], row[2],row[3]))

def readnameCompl():
  cursor.execute("""SELECT idPerson,name FROM nameCompl""")
  rows = cursor.fetchall()
  for row in rows:
    print('{0} : {1}'.format(row[0], row[1]))

def readName():
  cursor.execute("""SELECT idPerson,name FROM name""")
  rows = cursor.fetchall()
  for row in rows:
    print('{0} : {1}'.format(row[0], row[1]))


ratingdb(300000)
basicdb()
principalsdb()
#readBasics()
nameCompldb()
namedb()
#readName()
#namedb()
#readPrincipals()
conn.commit()
if (conn):
    conn.close()
#readRating()
#df=pd.read_csv('title.basics.tsv', sep='\t')
#readBasics()
#df.head()
