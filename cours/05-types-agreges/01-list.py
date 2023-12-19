# Création d'un liste
ma_liste = []

print(type(ma_liste))

fruits = ["pomme", "banane", "kiwi"]
print(fruits)

objets = ["pomme", 1, 2.5, True, ["kiwi"]]
print(objets)

# Extraire des informations
pomme = fruits[0]
print(pomme)

nombres = objets[1:3]
print(nombres)

kiwi = objets[4][0]
print(type(kiwi), kiwi)

# Ajouter des éléments
print("#" * 25)
nombres = [1, 2, 3, 4]
print(nombres)

# Ajouter à la fin avec .append()
nombres.append(5)
print(nombres)

# Ajouter à un indice donné
nombres.insert(0, -1)
nombres.insert(0, -1)
print(nombres)

# Compter le nombre d'occurrence d'un objet
print(nombres.count(-1))

# Supprimer par valeur
nombres.remove(-1)  # supprimer uniquement la première occurrence
print(nombres)

# Supprimer par indice
del nombres[0]
print(nombres)

# Longueur de la liste
print(len(nombres))

print("#" * 25)
# Opérateur d'appartenance in
fruits = ["pomme", "banane", "kiwi"]

if "banane" in fruits:
    print("Banane est dans la liste fruits.")

for fruit in fruits:
    print(fruit)

# Trier
nombres = [5, 42, -8, 45, 99]
nombres.sort(reverse=True)  # Attention, pas de retour en arrière.
print(nombres)

fruits.sort(reverse=True)
print(fruits)


a = [1, 2, 3]
b = a
b.append(50)
print(id(a), id(b))


import copy
b = copy.deepcopy(a)
print(id(a), id(b))