
import sqlite3


conn=sqlite3.connect('film.db')
cursor=conn.cursor()


def search(titre):
    cursor.execute("""SELECT * FROM basics WHERE titre=?""",(titre,))
    row = cursor.fetchall()[0]
    return row





# cursor.execute("""SELECT * FROM basics WHERE titre=?""",('12 Angry Men',))
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

cursor.execute("""SELECT * FROM ratings""")
print(cursor.fetchall())

print(search('Her'))
