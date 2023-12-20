import os
import shutil

# Copier des fichiers et dossiers
# On peut aussi renommer le nom de destination
# Attention, si le fichier existe, il sera écrasé.

chemin_repertoire = os.path.join(os.getcwd(), "data")
os.makedirs(chemin_repertoire, exist_ok=True)
src = os.path.join(os.getcwd(), "mon_dossier", "test.txt")
dst = os.path.join(chemin_repertoire, "test2.txt")
shutil.copy2(src, dst)

# copie récursive
src = os.path.join(os.getcwd(), "data")
dst = os.path.join(os.getcwd(), "data_backup")
# Le répertoire de destination ne DOIT pas exister.
shutil.copytree(src, dst)

# suppression récursive
shutil.rmtree(dst)

# déplacement
src = os.path.join(os.getcwd(), "data", "test2.txt")
dst = os.path.join(os.getcwd(), "mon_dossier")
shutil.move(src, dst)