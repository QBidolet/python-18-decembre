import os

print('#' * 50)
# A éviter : chemin absolu.
# Dépendant de la machine.
chemin = "C:\\users\\Quentin\\mon-projet\\fenetre.py"

# A faire : os.path.join
chemin = os.path.join(os.getcwd(), "mon_dossier")
print(chemin, type(chemin))

# création d'un dossier
os.makedirs(chemin, exist_ok=True)

# Vérifier l'existence d'un fichier
chemin_fichier = os.path.join(chemin, "test.txt")
print(os.path.isfile(chemin))
print(os.path.isfile(chemin_fichier))

# Changer de répertoire courant
os.chdir(chemin)
print(os.getcwd())

# Séparer l'extension du nom de fichier
nom, extension = os.path.splitext("mon_image.jpg")
print(nom, extension)

# Lister les dossiers et fichiers
liste_dossiers = os.listdir(os.getcwd())
print(liste_dossiers, type(liste_dossiers))
