import json,os,csv
import filmdb



class ListeFilm:
    def __init__(self,n):
        self.__name=n
        #self.__filename=n+".json"
        self.__filename=n+".csv"
        open(self.__filename)
        self.__liste=[]

    def get_name(self):
        return self.__name

    def get_fileName(self):
        return self.__filename

    def kill(self):
        os.remove(self.get_fileName())


    def addListeAttr(self,titre):
        movie=filmdb.Film(titre)
        self.__liste.append(movie)


    def add_Film(self,titre):
        movie=filmdb.Film(titre)
        #with open(self.get_fileName(),'w') as file:
        #    json.dump(movie.__dict__,file)
        with open(self.get_fileName(), mode='a') as Liste:
            liste_writer = csv.writer(Liste, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            liste_writer.writerow([movie.getTitleId(),movie.getTitle(),movie.getDate(),movie.getGenre(),movie.getNote(),movie.getVote(),movie.getDirector(),movie.getDirectorId(),movie.getActeurs(),movie.getActeursId()])
#            print(movie.getTitle())

        self.__liste.append(movie)


    def filter(self,filtre,categorie):
        if categorie=='director':
            for movie in self.getListe():
                # print(movie.getDirector()[0][0])
                if movie.getDirector()[0][0]==filtre:
                    print(movie.getTitle())

        if categorie=='titre':
            for movie in self.getListe():
                if movie.getTitle()==filtre:
                    print(movie.getTitle(),movie.getDirector())

        if categorie=='genre':
            for movie in self.getListe():
                print(movie.getGenre())
                    # if genre==filtre:
                    #     print(movie.getTitle())






    def getListe(self):
        return self.__liste
#    def retrieve(self,movie):


#
l=ListeFilm('testDB')
films=['Inception','Memento','Reservoir Dogs','Titanic','Shutter Island']
for f in films:
    l.add_Film(f)
print(l.getListe())
 #l.filter('Christopher Nolan','director')
# #l.filter('Memento','titre')
# l.filter('Thriller','genre')
