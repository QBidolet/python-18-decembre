"""
Exercice 3
Créer une fonction qui affiche les 20 premiers termes de la table de multiplication de 7.
Ensuite il faut rendre variable le nombre de termes et la table choisie.

Exemple :
1 x 7 = 7
2 x 7 = 14
3 x 7 = 21
...
20 x 7 = 140
"""


def generer_table_multiplication(table, nombre_terme):
    for i in range(1, nombre_terme + 1):
        resultat = i * table
        print(f"{i} x {table} = {resultat}")

generer_table_multiplication(10, 30)
