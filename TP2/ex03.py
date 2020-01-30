def csv_compare(f1, f2) :
	lst1 = []
	lst2 = []
	lst3 = []
	lecture1 = f1.readlines()
	lecture2 = f2.readlines()
	for ligne1 in lecture1 :
		test = 0
		for ligne2 in lecture2 :
			if ligne2 == ligne1 :
				lst3.append(ligne2)
				test = 1
				break
		if (test == 0) :
			lst1.append(ligne1)
	for ligne2 in lecture2 :
		if ligne2 not in lst3 :
			lst2.append(ligne2)
	print("Lignes uniquement présentes dans le premier fichier :")
	for elem in lst1 :
		print(elem, end='')
	print("Lignes uniquement présentes dans le second fichier :")
	for elem in lst2 :
		print(elem, end='')
	print("Lignes présentes dans les deux fichiers :")
	for elem in lst3 :
		print(elem, end='')

f1 = open("fichier1.csv")
f2 = open("fichier2.csv")
csv_compare(f1, f2)
f1.close()
f2.close()
