from voiture import Voiture


class VoitureDeCourse(Voiture):
    def __init__(self, couleur, marque, vitesse):
        Voiture.__init__(self, couleur, marque)
        self.vitesse = vitesse

    def __str__(self):
        return super().__str__() + f"avec une vitesse de {self.vitesse}km/h."
        # return (f"Voiture : {self.marque} de couleur {self.couleur}"
        #         f" avec une vitesse de {self.vitesse}km/h.")


voiture_de_course = VoitureDeCourse("Rouge", "Tesla", 350)
print(voiture_de_course)
voiture_de_course.klaxonner()