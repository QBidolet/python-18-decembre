# Lever une exception
# while True:
#     try:
#         nombre = input("Entrez un nombre.")
#         nombre = int(nombre)
#         print(nombre)
#         break
#     except ValueError:
#         print("Veuillez taper un nombre.")

# Double exception
try:
    numerateur = int(input("Entrez un numérateur\n"))
    denominateur = int(input("Entrez un dénominateur\n"))
    resultat = numerateur / denominateur
except ValueError:
    print("Veuillez entrer un nombre valide.")
except ZeroDivisionError:
    print("Le dénominateur doit être différent de 0.")
# except (ValueError, ZeroDivisionError) as error:
#     # print("Nombre invalide.")
#     print(error)


# Lever une exception manuellement
fichier = open("fichier.txt")
try:
    fichier.read()
except Exception as e:
    fichier.close()
    raise Exception(e)
# finally:
#     fichier.close()

nombre = input("Entrez un nombre positif")
if int(nombre) < 0:
    raise ValueError("Le nombre est négatif.")
