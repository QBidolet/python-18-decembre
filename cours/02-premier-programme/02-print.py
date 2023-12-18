print("Hello World!")

# Plusieurs arguments
print("Hello", "World!")

# Modifier le séparateur
print("Hello", "World!", sep="/")

# Modifier le end
print("Hello", "World!", end="\n\n")
print("Hello World!")

phrase = "Salut!"

# Concaténer
print(phrase + " Comment ça va ?")

# Retour à la ligne avec \n
print("Ligne 1.\nLigne 2.")

# Plusieurs lignes : chaine de caractère multiligne
print("""
    *** QCM ***
    Bienvenue dans le QCM.
    Je vais vous poser 4 questions etc.
""")


"""
Exercice : Afficher le texte suivant.
5-6$$$
7$$$
8
"""
print("5-6$$$\n7$$$\n8")
print("""5-6$$$
7$$$
8
""")
print("5", "6", sep="-", end="$$$\n")
print("7", end="$$$\n")
print(8)