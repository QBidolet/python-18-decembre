# Création d'une fonction
def do_nothing():
    pass


print(type(do_nothing))


def somme(a, b, c):
    # Fonction : renvoit une valeur
    return a + b + c


resultat = somme(1, 2, 3)
print(resultat)


def menu(entree="Salade", plat="Frites", dessert="Mousse au chocolat"):
    # Procédure : ne renvoit rien.
    print(f"\t*** MENU ***\n"
          f"\t\tEntrée : {entree}\n"
          f"\t\tPlat : {plat}\n"
          f"\t\tDessert : {dessert}")


menu()

# Paramètres positionnels
menu("Foie gras", "Huitres", "Bûche")

# Paramètres nommés
menu(plat="Huitres", entree="Foie gras", dessert="Bûche")

# On peut mélanger les deux
menu("Foie gras", dessert="Bûche", plat="Huitres")

menu(plat="Huitre")

# Exemple
print("Une", "phrase", "aussi", "longue", "que", "je", "veux", sep="-", end="\n")


# *args
def somme(*args):
    print(type(args))
    resultat = 0
    for arg in args:
        resultat += arg
    return resultat


resultat = somme(55, 25, 20, 20, 14)
print(resultat)


# **kwargs
def menu(**kwargs):
    print(type(kwargs))
    for cle, valeur in kwargs.items():
        cle = cle.capitalize().replace("_", " ")
        print(f"{cle} : {valeur}")


menu(entree="Salade", plat_poisson="Huitre", plat_viande="Dinde", dessert="Bûche")


# fonctions génératrices
def range_2(n):
    compteur = 0
    while compteur < n:
        yield compteur
        compteur += 1


resultat = range_2(6)

print(next(resultat))
print(next(resultat))
print(next(resultat))
print(next(resultat))
print(next(resultat))
print(next(resultat))

resultat = range_2(6)

print(type(resultat))

for i in range_2(6):
    print(i)

# Fonctions anonymes
print('#' * 25)


def double(nombre):
    return nombre * 2


liste = [1, 2, 3, 4]
# nouvelle_liste = []
# for nombre in liste:
#     nouvelle_liste.append(double(nombre))
# print(nouvelle_liste)

# mon_map = map(double, liste)
# print(list(mon_map))

# map : va appliquer une transformation à une fonction et sauvegarder le résultat.
mon_map = map(lambda x: x * 2, liste)
print(list(mon_map))

# filter : permet de filtrer une liste sur une condition
mon_filter = filter(lambda x: x % 2 == 0, liste)
print(list(mon_filter))