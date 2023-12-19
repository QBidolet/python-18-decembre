personne = {
    "nom": "BIDOLET",
    "prenom": "Quentin",
    "age": 29
}

print(personne, type(personne))

# Accéder à un élément
print(personne["age"])

print("#" * 25)
# Parcourir un dictionnaire
for cle in personne.keys():
    print(cle)

print("#" * 25)
for valeur in personne.values():
    print(valeur)

print("#" * 25)
for cle, valeur in personne.items():
    print(cle, ":", valeur)


if "Quentin" in personne.values():
    print("La valeur Quentin est présente dans le dictionnaire.")


# Assignation
personne["prenom"] = "Romain"
print(personne)

# Exemple
users = {
    "125A": {
        "nom": "DUPONT",
        "prenom": "Jean",
        "metiers": ["cariste, chef d'équipe"]
    },
    "1258D": {
        "nom": "BIDOLET",
        "prenom": "Quentin",
        "metiers": ["informaticien, chef d'équipe"]
    }
}
