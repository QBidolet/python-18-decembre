"""
Vous devez écrire un programme qui demande à l'utilisateur de saisir une vitesse en miles/heure.
 et vous devez afficher cette vitesse en km/h et m/s.

BONUS :
Vous devez réinviter votre utilisateur à saisir une valeur une fois
la conversion terminé et boucler de cette manière.

Indication pour la conversion : pour passer des miles/heure au mètre par seconde il faut diviser par 2.237
Indication pour la conversion : pour passer des miles/heure au km par heure il faut multiplier par 1.609
"""

continuer = "oui"
while continuer == "oui":
    saisie = float(input("Veuillez saisir une vitesse en miles/heure.\n"))
    m_s = saisie / 2.237
    km_h = saisie * 1.609
    print(f"{km_h} km/h\n{m_s} mètre par seconde.")
    continuer = input("Voulez-vous continuer ?\n")
    continuer = continuer.lower()
