a = 0

print(type(a))

a = 1.1
print(type(a))

# Convertir en entier
a = int(a)
print(a)

# Convertir en chaine de caractère
a = str(a)
print(a, type(a))

# Exemple saisie utilisateur
# Attention, un input retourne TOUJOURS un str (chaine de caractère)
# Convertir en réel.
nombre = float(input("Veuillez saisir un nombre"))
# nombre = float(nombre)
print(type(nombre))
resultat = nombre / 2
print(resultat)

# Convertir en booléen
vrai = bool(1)
print(type(vrai))

# Attention, toutes les conversions ne sont pas possibles.
int("Je suis pas un nombre.")
