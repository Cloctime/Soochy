import json,os
import Film



class ListeFilm:
    def __init__(self,n):
        self.__name=n
        self.__filename=n+".json"
        open(self.__filename,'w')

    def get_name(self):
        return self.__name

    def get_fileName(self):
        return self.__filename

    def kill(self):
        os.remove(self.get_fileName())


    def add_Film(self,movie):
        movie=Film.Film(movie)
        with open(self.get_fileName(),'w') as file:
            json.dump(movie.__dict__,file)

#    def retrieve(self,movie):



l=ListeFilm('salut')

films=['Inception']
for f in films:
    l.add_Film(f)
