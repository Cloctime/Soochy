import csv

class Film:
    def __init__(self,name):

        #recuperation du film dans la bdd title.basics via le titre pour l'id du titre, le titre, la date de sortie et les genres
        with open('title.basics.tsv') as tsvfile:
          reader = csv.reader(tsvfile, delimiter='\t')
          for row in reader:
              if row[3]==name:
                  film=row
                  break;
        self.__titleId=film[0]
        self.__title=film[3]
        self.__date=film[5]
        self.__genre=film[8]

        #avec l'id du film on trouve l'id du realisateur
        with open('title.crew.tsv') as tsvfile:
            reader = csv.reader(tsvfile, delimiter='\t')
            for row in reader:
                if row[0]==self.__titleId:
                    film=row
                    break;
        self.__directorId=film[1]

        #avec l'id du realisateur on retrouve le nom du realisateur et d'autre film qu'il a fait
        with open('name.basics.tsv') as tsvfile:
            reader = csv.reader(tsvfile, delimiter='\t')
            for row in reader:
                if row[0]==self.__directorId:
                    film=row

        self.__director=film[1]
        self.__autreFilm=film[5]

        with open('title.principals.tsv') as tsvfile:
            film=[]
            reader = csv.reader(tsvfile, delimiter='\t')
            for row in reader:
                if row[0]==self.__titleId:
                    film.append(row)

        acteursId=[]
        for person in film:
            if person[3]=='actor' or person[3]=='actress':
                acteursId.append(person[2])

        self.__acteursId=acteursId

        acteurs=[]
        for acteurId in self.__acteursId:
            with open('name.basics.tsv') as tsvfile:
                reader = csv.reader(tsvfile, delimiter='\t')
                for row in reader:
                    if row[0]==acteurId:
                        acteurs.append(row[1])

        self.__acteurs=acteurs



    def getTitleId(self):
        return self.__titleId

    def getTitle(self):
        return self.__title

    def getDate(self):
        return self.__date

    def getGenre(self):
        return self.__genre

    def getDirectorId(self):
        return self.__directorId

    def getDirector(self):
        return self.__director

    def getAutre(self):
        return self.__autreFilm

    def getActeursId(self):
        return self.__acteursId

    def getActeurs(self):
        return self.__acteurs





'''
c=Film('Pulp Fiction')
print(c.getTitleId())
print(c.getTitle())
print(c.getDate())
print(c.getDirectorId())
print(c.getDirector())
print(c.getAutre())
#print(c.getActeurs())
#print(c.getActeursId())

c=Film('Toy Story')
#c2=Film('men in black')
'''
#c=Film('Shutter Island')
#print(c)
