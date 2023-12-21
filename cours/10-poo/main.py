from voiture import Voiture

voiture = Voiture("Rouge", "Tesla")
print(voiture.couleur, voiture.marque)
voiture.klaxonner()
voiture.repeindre("Jaune")
print(voiture.couleur)