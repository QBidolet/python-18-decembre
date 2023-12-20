"""
Vous devez construire un organisateur
de fichier à partir de ce dictionnaire.
Le programme scannera un dossier
dans lequel il y a des fichiers (text, pdf ...)
et devra créer le dossier correspondant
au clé du dictionnaire, si durant le scan
on trouve des fichiers il faudra les déplacer
dans le dossier correspondant.
Exemple : dans mon dossier il y a un fichier .pdf,
le programme doit créer le dossier PDF
et déplacer le fichier à l'intérieur.

BONUS :
3 manières de faire, implémentez les toutes. (pour itérer sur les fichiers/dossiers).
Cherchez dans la documentation les deux autres.
"""
import os
import shutil

folder_dict = {
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg",
               ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"],
    "DOCUMENTS": [".doc", ".pptx", ".docx", ".doc", ".xla"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", ".ogg", ".oga", ".raw", ".vox", ".wav", ".wma"],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "XML": [".xml"],
    "EXE": [".exe"]
}

chemin_a_trier = os.path.join(os.getcwd(), "a trier")


# Méthode 1
# for nom_fichier in os.listdir(chemin_a_trier):
#     _, extension = os.path.splitext(nom_fichier)
#     for repertoire, extensions in folder_dict.items():
#         # Chercher si l'extension du fichier est dans la liste d'extensions.
#         if extension in extensions:
#             # Une fois trouvé, créer si nécessaire le dossier de destination
#             chemin_dossier = os.path.join(os.getcwd(), repertoire)
#             os.makedirs(chemin_dossier, exist_ok=True)
#             # Copier le fichier dans le répertoire.
#             chemin_fichier = os.path.join(chemin_a_trier, nom_fichier)
#             shutil.copy(chemin_fichier, chemin_dossier)

# Méthode 2
# for element in os.scandir(chemin_a_trier):
#     if element.is_file():
#         _, extension = os.path.splitext(element.name)
#         for repertoire, extensions in folder_dict.items():
#             if extension in extensions:
#                 chemin_dossier = os.path.join(os.getcwd(), repertoire)
#                 os.makedirs(chemin_dossier, exist_ok=True)
#                 chemin_fichier = os.path.join(chemin_a_trier, element.name)
#                 shutil.copy(chemin_fichier, chemin_dossier)

# Méthode 3 os.walk
# print(os.walk(chemin_a_trier))
for repertoire, sous_repertoires, fichiers in os.walk(chemin_a_trier):
    for fichier in fichiers:
        _, extension = os.path.splitext(fichier)
        for nouveau_repertoire, extensions in folder_dict.items():
            if extension in extensions:
                chemin_dossier = os.path.join(os.getcwd(), nouveau_repertoire)
                os.makedirs(chemin_dossier, exist_ok=True)
                chemin_fichier = os.path.join(repertoire, fichier)
                shutil.copy(chemin_fichier, chemin_dossier)


