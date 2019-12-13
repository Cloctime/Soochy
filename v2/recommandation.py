import csv
import filmdb
import listefilmdb
import recover

real_fav_top={}
genre_fav_top={}
decenie_fav_top={}
acteur_fav_top={}
genre_fav = {}
decenie_fav = {}
acteur_fav = {}
real_fav= {}

Film={}

def create():
	li=listefilmdb.ListeFilm('testDB')
	films=['Inception','Memento','Reservoir Dogs','Titanic','Shutter Island']
	for f in films:
			li.add_Film(f)
	return li


liste_fav=create()

def attributionPoints(param,liste):
	if param=='acteur' or param=='decenie':
		if param=='acteur':
			score=4
			dic=acteur_fav
			for f in liste.getListe() :
				t=0
				chaine = f.getActeursId()
				for t in range(0,len(chaine)):
					if chaine[t] not in dic.keys():
				 		dic[chaine[t]]=score
					else:dic[chaine[t]]=dic[chaine[t]]+score

		if param=='decenie':
			score=6
			dic=decenie_fav
			for f in liste.getListe() :
				l=round((f.getDate()/10))*10
				if l not in dic.keys():
					dic[l] = score
				else :dic[l] =dic[l] +score


	if param=='director':
		score=5
		dic=real_fav
		for f in liste.getListe() :
			l=f.getDirectorId()
			if l not in dic.keys():
				dic[l] = score
			else :dic[l] =dic[l] +score
	if param=='genre':
		score=2
		dic=genre_fav
		for f in liste.getListe():
			l=f.getGenre()
			if l not in dic.keys():
				dic[l] = score
			else :dic[l] =dic[l] +score


def Top(param_top,param):
	acteur=param
	a=len(param_top)
	b=len(acteur)
	while (len(param_top) <= 20)and(len(acteur)!=0) :
		Addacteur(acteur,param_top)


def Addacteur(acteur,param_top):
	k=0
	for elem, value in acteur.items():
		if k<=value:
			k=value
			u=elem
	param_top[u]=k
	del acteur[u]




def Recommandation():
	Top(real_fav_top,real_fav)
	Top(genre_fav_top,genre_fav)
	Top(decenie_fav_top,decenie_fav)
	Top(acteur_fav_top,acteur_fav)
	listeprovisoire=[]
	attributionPoints('acteur',liste_fav)
	attributionPoints('decenie',liste_fav)
	attributionPoints('director',liste_fav)
	attributionPoints('genre',liste_fav)
	Top(acteur_fav_top,acteur_fav)
	complet=recover.recover('completeListe')
	for p in real_fav_top.keys():
		for l in genre_fav_top.keys():
			resultat=complet.DoubleFilter(p,'director',l,'genre')
			for f in resultat.getListe():
				if f not in listeprovisoire:
					listeprovisoire.append(f)
	for p in real_fav_top.keys():
		for l in decenie_fav_top.keys():
			resultat=complet.DoubleFilter(p,'director',l,'decenie')
			for f in resultat.getListe():
				if f not in listeprovisoire:
					listeprovisoire.append(f)
	for p in genre_fav_top.keys():
		for l in decenie_fav_top.keys():
			resultat=complet.DoubleFilter(p,'genre',l,'decenie')
			for f in resultat.getListe():
				if f not in listeprovisoire:
					listeprovisoire.append(f)
	print(listeprovisoire)

# attributionPoints('genre')
attributionPoints('acteur',liste_fav)
#print(acteur_fav)
attributionPoints('decenie',liste_fav)
# print(decenie_fav)
attributionPoints('director',liste_fav)
#print(real_fav)
attributionPoints('genre',liste_fav)
#print(genre_fav)
Top(acteur_fav_top,acteur_fav)
# print(acteur_fav_top)
Recommandation()






# def Couple():
# 	Top(real_fav_top,real_fav)
# 	Top(genre_fav_top,genre_fav)
# 	Top(decenie_fav_top,decenie_fav)
# 	Top(acteur_fav_top,acteur_fav)
# 	listeprovisoire=[]
# 	for p in real_fav_top.keys():
# 		for l in genre_fav_top.keys():
# 			CoupleRecherche.append(p)
# 			CoupleRecherche.append(l)
# 	for p in real_fav_top.keys():
# 		for l in decenie_fav_top.keys():
# 			CoupleRecherche.append(p)
# 			CoupleRecherche.append(l)
# 	for p in genre_fav_top.keys():
# 		for l in decenie_fav_top.keys():
# 			CoupleRecherche.append(p)
# 			CoupleRecherche.append(l)

# def testfiltre1():
# 	l=recover.recover('completeListe')
# 	for r in acteur_fav_top.keys():
# 		resultat=l.filter(r,'acteur')
# def testfiltre2():
# 	l=recover.recover('completeListe')
# 	for r in real_fav_top.keys():
# 		resultat=l.filter(r,'director')
# def testfiltre():
# 	l=recover.recover('completeListe')
# 	for r in decenie_fav_top.keys():
# 		resultat=l.filter(r,'decenie')
# 		print(resultat)
# #
# def testdoublefiltre():
# 	l=recover.recover('completeListe')
# 	resultat=l.DoubleFilter('nm0634240','director',"Action,Adventure,Sci-Fi",'genre')
