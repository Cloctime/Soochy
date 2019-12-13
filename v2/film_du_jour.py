from datetime import datetime
import filmdb
import listefilmdb
import recover
import random
def create():
	li=listefilmdb.ListeFilm('FDJ')
	films=['Inception','Memento','Reservoir Dogs','Titanic','Shutter Island']
	for f in films:
			li.add_Film(f)
	return li

def selection():
    selection=create()
    date = datetime.now().strftime("%d/%m/%y")
    file= open("date.txt", 'r')
    dateprev = file.read()
    file.close()
    if dateprev != date :
        file= open("date.txt", 'w')
        file.write(date)
        file.close()
        n = random.randint(0,len(selection.getListe()))
        print(selection.getListe()[n])

create()
selection()
