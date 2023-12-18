# Echappement avec \
ma_phrase = 'J\'ai mon masque.'
ma_phrase = "J'ai mon masque."
ma_phrase = "J'ai mon masque.\n\tEt je suis content."
print(ma_phrase)

# Concaténation avec +
prenom = "Quentin"
nom = "BIDOLET"

# Manière simple
print("Je m'appelle " + prenom + " " + nom + ".")

# version python 2
ma_phrase = "Je m'appelle %s %s." % (prenom, nom)
print(ma_phrase)

# version python 3
ma_phrase = "Je m'appelle {0} {1}.".format(prenom, nom)

# version pythonic
ma_phrase = f"Je m'appelle {prenom} {nom}."
print(ma_phrase)

# dupliquer avec *
print("#" * 25)

# Extraction de chaine de caractère.
alphabet = "abcdefghij"

# Premier élément, commence à l'indice 0.
print(alphabet[0])
print(alphabet[1])

# [start : end : step]
# start : end
print(alphabet[0:3])

# Valeurs par défaut
# start = 0
# end = longueur de la chaine de caractère.
# step = 1
print(alphabet[2:])
print(alphabet[:5])
print(alphabet[::3])

# valeurs négatives
# extraire à l'envers
print(alphabet[::-1])
# extraire toute la chaine sauf les deux dernières lettres
print(alphabet[:-2])

# extraire les trois dernières lettres
print(alphabet[-3:])

# Quelques méthodes utiles
phrase = "salut"
print(phrase.capitalize())
print(phrase.upper())
print(phrase.lower())
print(phrase.replace("a", "e"))

# Exemple concret
nom = "queNtiN"
nom = nom.lower().capitalize()
print(nom)

phrase = "une phrase un peu longue"
print(phrase.title())
