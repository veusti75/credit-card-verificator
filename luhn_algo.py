## Algorithme de Luhn

def luhn(string_numero_carte):
	global c

	#Affiche numéro CC backwards
	numero_carte = string_numero_carte[::-1]

	# Tous les éléments de la liste sont des int
	int_numero_carte = [int(n) for n in numero_carte]
	
	# Double tous les deux chiffres
	int_numero_carte[1::2] = [n*2 for n in int_numero_carte[1::2]]
	# De-concatenate les nombres à deux chiffres
	int_numero_carte[1::2] = [n+1 if n>9 else n+0 for n in int_numero_carte[1::2] ]
	int_numero_carte[1::2] = [n%10 for n in int_numero_carte[1::2]]

	# Somme tous les éléments de la liste
	somme = sum(int_numero_carte)

	# Vérification validité CC
	if somme % 10 == 0:
		# condition type
		c=0	
		print("La carte est valide.")
		c+=1
	else:
		print("La carte est non valide.")


	

	


	


