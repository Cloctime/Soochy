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

    def vider(self):
        self.__liste.clear()

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
        retour=[]
        if categorie=='director':
            for movie in self.getListe():
                #print(movie.getDirectorId()[0][0])
                if movie.getDirectorId()==filtre:
                    retour.append(movie)
            return(retour)

        if categorie=='titre':
            for movie in self.getListe():
                if movie.getTitle()==filtre:
                    retour.append(movie)
            return(retour)


        if categorie=='genre':
            for movie in self.getListe():
                if movie.getGenre()==filtre:
                    retour.append(movie)
            return(retour)

        if categorie=='acteur':
            for movie in self.getListe():
                #print(movie.getDirectorId()[0][0])
                for t in range(0,len(movie.getActeursId())):
                    if movie.getActeursId()[t]==filtre:
                        retour.append(movie)
            return(retour)

        if categorie=='decenie':
            for movie in self.getListe():
                if filtre <= movie.getDate()<=filtre+9:
                    retour.append(movie)
            return(retour)



    def DoubleFilter(self,filtre,categorie,filtre2,categorie2):
        temp=ListeFilm('recherche')
        li=[]
        films=self.filter(filtre,categorie)
        for f in films:
            temp.add_Film(f.getTitle())
        filmsRetour=temp.filter(filtre2,categorie2)
        temp.vider()
        for f in filmsRetour:
            temp.add_Film(f.getTitle())
        return temp





    def getListe(self):
        return self.__liste
#    def retrieve(self,movie):
# l=ListeFilm('testDB')
# films=['Inception','Memento','Reservoir Dogs','Titanic','Shutter Island']
# for f in films:
#     l.add_Film(f)
# print(l.getListe())
#l.filter('Christopher Nolan','director')
#l.filter('Memento','titre')
#l.filter('Thriller','genre')
