## Vérification type CC

def type(string_numero_carte):

	print(string_numero_carte)
	int_numero_carte = int(string_numero_carte)

	# Check le premier / deux premiers chiffres de la CC
	first_digit = int_numero_carte
	two_first_digits = int((string_numero_carte)[:2])

	# Critères correspondance CC VISA
	while (first_digit >= 10):
		first_digit=first_digit // 10
		if first_digit == 4 and len(string_numero_carte) == 13 or first_digit == 4 and len(string_numero_carte) == 16:
				print("VISA")

	# Critères correspondance CC MasterCard
	if two_first_digits >=51 and two_first_digits <=55 and len(string_numero_carte) == 16:
		print("MasterCard")

	# Critères correspondance CC American Express
	if two_first_digits == 34 and len(string_numero_carte) == 15 or two_first_digits == 37 and len(string_numero_carte) == 15:
		print("American Express")

	# Critères correspondance CC Maestro
	if two_first_digits == 50 and len(string_numero_carte) == 12 or two_first_digits == 50 and len(string_numero_carte) == 19 or two_first_digits >=56 and two_first_digits <=59 and len(string_numero_carte) == 12 or two_first_digits >=56 and two_first_digits <=59 and len(string_numero_carte) == 19:
		print("Maestro")



	