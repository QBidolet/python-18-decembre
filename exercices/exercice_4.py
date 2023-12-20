"""
écrire un programme qui demande de saisir, en anglais dans un premier temps,
le nom d'un mois et le programme retourne le nombre de jour de ce mois.

BONUS :
Donner la posibilité à l'utilisateur de saisir un mois en français également.
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
frTranslator = {
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