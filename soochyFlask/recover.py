import csv
import listefilmdb



def recover(name):
    filename=name+".csv"
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        l=listefilmdb.ListeFilm(name)
        for row in csv_reader:
#            print(row[1])
            l.addListeAttr(row[1])

    return l


l=recover('completeListe')
l.filter('Christopher Nolan','director')
# for film in l.getListe():
#  print(film.getDirector())
# print(l.getListe())
# l.add_Film('avengers')
# print(l.getListe())
