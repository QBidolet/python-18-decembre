# ouvrir / lire / écrire
# 4 modes d'ouvertures :
# r : pour la lecture seule
# w : écriture, écrase le contenu existant.
# a : ajouter à la fin du fichier
# x : écrire seulement si le fichier n'existe pas.
fichier = open("mon_fichier.txt", "wt")
fichier.write("Hello World!")
fichier.close()
# Tout ce qui s'ouvre, se ferme.

fichier = open("mon_fichier.txt", "a")
fichier.write("\nDeuxième ligne.")
fichier.close()

# Lire tout le contenu d'un coup avec .read()
fichier = open("mon_fichier.txt", "r")
contenu = fichier.read()
print(contenu, type(contenu))
fichier.close()

print("#" * 25)
# Lire ligne par ligne avec readlines()
fichier = open("mon_fichier.txt")
for ligne in fichier.readlines():
    print(ligne)
fichier.close()

print("#" * 25)
# Exemple de lecture / écriture
with open('mon_fichier.txt', "r") as fichier:
    contenu = fichier.read()
    print(fichier.read())
    # .tell() donne l'indice du curseur.
    print(fichier.tell())
    # .seek() pour se positionner à un indice donné
    fichier.seek(0)
    print(fichier.read())

contenu *= 2

with open('mon_fichier.txt', "w") as fichier:
    fichier.write(contenu)
