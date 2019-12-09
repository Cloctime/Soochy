import listefilmdb
import sqlite3

conn=sqlite3.connect('film.db')
cursor=conn.cursor()

def filmCSV():
    liste=listefilmdb.ListeFilm('completeListe')
    cursor.execute("""SELECT titre FROM basics""")
    rows=cursor.fetchall()
    for row in rows:
        # print(row[0])
        liste.add_Film(row[0])
    print('ok')

filmCSV()
