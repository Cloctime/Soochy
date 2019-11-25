import json,os,csv
import Film



class ListeFilm:
    def __init__(self,n):
        self.__name=n
        #self.__filename=n+".json"
        self.__filename=n+".csv"
        open(self.__filename,'w')

    def get_name(self):
        return self.__name

    def get_fileName(self):
        return self.__filename

    def kill(self):
        os.remove(self.get_fileName())


    def add_Film(self,movie):
        movie=Film.Film(movie)
        #with open(self.get_fileName(),'w') as file:
        #    json.dump(movie.__dict__,file)
        with open(self.get_fileName(), mode='a') as Liste:
            liste_writer = csv.writer(Liste, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            liste_writer.writerow([movie.getTitleId(),movie.getTitle(),movie.getDate(),movie.getGenre(),movie.getAutre(),movie.getDirector(),movie.getDirectorId(),movie.getActeurs(),movie.getActeursId()])
            print(movie.getTitle())


#    def retrieve(self,movie):



l=ListeFilm('tests')
films=['Inception','Memento','Reservoir Dogs','Seven','Shutter Island']
for f in films:
    l.add_Film(f)
