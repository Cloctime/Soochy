import csv
import sqlite3

conn=sqlite3.connect('film.db')
cursor=conn.cursor()

# Select id from sometable where name like '%omm%'

class Film:
    def __init__(self,titre):

        #recuperation du film via son nom dans la bdd basics
        cursor.execute("""SELECT * FROM basics WHERE titre like ? COLLATE NOCASE""",('%'+titre+'%',))
        film= cursor.fetchall()[0]

        self.__titleId=film[0]
        self.__title=film[2]
        self.__date=film[3]
        self.__duration=film[4]
        self.__genre=film[5]


        #recuperation des id's du realisateur et des acteurs dans la bdd principals via l'id du film
        acteurs=[]
        self.__directorId=0
        cursor.execute("""SELECT idPerson,job FROM principals WHERE id=?""",(self.__titleId,))
        persons=cursor.fetchall()
        for person in persons:
            if person[1]=='director':
                self.__directorId=person[0]
            if person[1]=='actor'or person[1]=='actress':
                acteurs.append(person[0])

        # self.__directorId=director[0]
        self.__acteursId=acteurs


        #recuperation du nom du realisateur dans la bdd name via l'id du realisateur
        self.__director="inconnu"
        if self.__directorId:
            cursor.execute("""SELECT DISTINCT name FROM name WHERE idPerson=?""",(self.__directorId,))
            self.__director=cursor.fetchall()

        #recuperation des noms des acteurs dans la bdd name via les id's des acteurs
        self.__acteurs=[]
        for acteurId in self.__acteursId:
            cursor.execute("""SELECT DISTINCT name FROM name WHERE idPerson=?""",(acteurId,))
            self.__acteurs.append(cursor.fetchall())


        cursor.execute("""SELECT average,vote FROM ratings WHERE id=?""",(self.__titleId,))
        film=cursor.fetchall()
        self.__note=film[0][0]
        self.__vote=film[0][1]


    def getTitleId(self):
        return self.__titleId

    def getTitle(self):
        return self.__title

    def getDuration(self):
        return self.__duration

    def getDate(self):
        return self.__date

    def getGenre(self):
        return self.__genre

    def getDirectorId(self):
        return self.__directorId

    def getDirector(self):
        return self.__director

#    def getAutre(self):
#        return self.__autreFilm

    def getActeursId(self):
        return self.__acteursId

    def getActeurs(self):
        return self.__acteurs

    def getNote(self):
        return self.__note

    def getVote(self):
        return self.__vote


# c=Film('citizen kane')
# print(c.getTitleId())
# print(c.getTitle())
# print(c.getDate())
# print(c.getDuration())
# print(c.getGenre())
#
# print(c.getDirectorId())
# print(c.getDirector())
# #print(c.getAutre())
# print(c.getActeurs())
# print(c.getActeursId())
# print(c.getNote())
# print(c.getVote())


#c=Film('Toy Story')
#c2=Film('men in black')

#c=Film('Shutter Island')
#print(c)
