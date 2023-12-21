"""
écrire un programme qui demande de saisir, en anglais dans un premier temps,
le nom d'un mois et le programme retourne le nombre de jour de ce mois.

BONUS :
Donner la possibilité à l'utilisateur de saisir un mois en français également.
"""

# Un dictionnaire d'association nom de mois / jour
months = {
    "january": 31,
    "february": 28,
    "march": 31,
    "april": 30,
    "may": 31,
    "june": 30,
    "july": 31,
    "august": 31,
    "september": 30,
    "october": 31,
    "november": 30,
    "december": 31
}
# Un second dictionnaire d'association des noms de mois français / anglais
fr_translator = {
    "janvier": "january",
    "février": "february",
    "mars": "march",
    "avril": "april",
    "mai": "may",
    "juin": "june",
    "juillet": "july",
    "août": "august",
    "septembre": "september",
    "octobre": "october",
    "novembre": "november",
    "décembre": "december"
}


def traduire_mois_francais_vers_anglais(mois):
    if mois in fr_translator:
        mois = fr_translator[mois]
    return mois

def obtenir_nombre_jour_par_mois(mois):
    nombre_jour = 0
    if mois in months.keys():
        nombre_jour = months[mois]
    return nombre_jour

mois_input = input("Entrez le mois en anglais ou en français.\n").lower()
mois_input = traduire_mois_francais_vers_anglais(mois_input)
nombre_jour = obtenir_nombre_jour_par_mois(mois_input)

if nombre_jour:
    print(f"Le mois {mois_input} a {nombre_jour} jours.")
else:
    print(f"Le mois {mois_input} n'existe pas en français ni en anglais.")

