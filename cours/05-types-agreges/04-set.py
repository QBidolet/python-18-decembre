# ensemble désordonné sans doublon

prenoms = {
    "Quentin",
    "Jean",
    "Romain"
}

print(type(prenoms))
prenoms.add("Frédéric")
print(prenoms)

prenoms.remove("Romain")
print(prenoms)

for prenom in prenoms:
    print(prenom)

if "Quentin" in prenoms:
    print("Quentin est dans le set.")

ma_liste = [1, 5, 2, 4, 5, 5]
valeurs_uniques = set(ma_liste)
print(valeurs_uniques)
