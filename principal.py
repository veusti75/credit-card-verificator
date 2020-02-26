import luhn_algo
from type_CC import type
from luhn_algo import luhn


string_numero_carte = input("Veuillez entrer votre numéro de CC:")
while string_numero_carte !="aucun":

	# Vérifie la validité de la carte
	luhn(string_numero_carte)

	# Retourne le type de la CC
	if luhn_algo.c == 1:
		type(string_numero_carte)

	string_numero_carte = input("Veuillez entrer votre numéro de CC:")