import csv

file = 'tests.csv'
Film=[]
with open(file) as fh:
	rd = csv.DictReader(fh, delimiter=',')
	for row in rd:
		Film.append(row)
real_fav_top={}
genre_fav_top={}
decenie_fav_top={}
acteur_fav_top={}
genre_fav = {}
decenie_fav = {}
acteur_fav = {}
real_fav= {}







def attributionPoints(param):
	if param=='acteur' or param=='decenie':
		if param=='acteur':
			score=4
			dic=acteur_fav
			for f in Film :
				chaine = f['acteur']
				caractere = ","
				for x in chaine.split(caractere):
					l=x.strip("[] '' ")
					if l not in dic.keys():
						dic[l] = score
					else :dic[l] =dic[l] +score

		if param=='decenie':
			score=6
			dic=decenie_fav
			for f in Film :
				l=f['an'][:3]
				if l not in dic.keys():
					dic[l] = score
				else :dic[l] =dic[l] +score

	else:
		if param=='real':
			score=5
			dic=real_fav
		if param=='genre':
			score=2
			dic=genre_fav
		for f in Film:
			l=f[param]
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

CoupleRecherche=[]



def Couple():
	for p in real_fav_top.keys():
		for l in genre_fav_top.keys():
			CoupleRecherche.append(p)
			CoupleRecherche.append(l)
	for p in real_fav_top.keys():
		for l in decenie_fav_top.keys():
			CoupleRecherche.append(p)
			CoupleRecherche.append(l)
	for p in genre_fav_top.keys():
		for l in decenie_fav_top.keys():
			CoupleRecherche.append(p)
			CoupleRecherche.append(l)




attributionPoints('genre')
attributionPoints('acteur')
attributionPoints('real')
attributionPoints('decenie')
Top(acteur_fav_top,acteur_fav)
Top(real_fav_top,real_fav)
Top(genre_fav_top,genre_fav)
Top(decenie_fav_top,decenie_fav)
print(acteur_fav_top)
Couple()
print(CoupleRecherche)
