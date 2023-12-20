class Voiture:
    def __init__(self, couleur, marque):
        self.couleur = couleur
        self.marque = marque


voiture = Voiture("Rouge", "Tesla")
print(voiture.couleur, voiture.marque)

mercedes = Voiture("Noire", "Mercedes")
print(mercedes.marque)