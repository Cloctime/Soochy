import csv

file = 'tests.csv'
Film=[]
with open(file) as fh:
	rd = csv.DictReader(fh, delimiter=',')
	for row in rd:
		Film.append(row)

genre_fav = {}
annee_fav = {}
acteur_fav = {}
real_fav= {}

def attributionPoints(param):
	if param=='acteur':
		score=4
		dic=acteur_fav
		for f in Film :
			chaine = f['acteur']
			caractere = ","
			for x in chaine.split(caractere):
				l=x.strip("[] ''")
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



#def Trier(a):
#	l=a
#	a={}
#	for i in range(0,len(l)):
#		k=0
#		for elem, value in l.items():
#			i=i+1
#			if k<value:
#				k=value
#				u=elem
#		b[u]=k
#		del l[o]
#
#	return(a)











attributionPoints('genre')
attributionPoints('acteur')
attributionPoints('real')

print(real_fav)
