"""
Définissez une classe CompteBancaire(), qui permet d’instancier des objets tels que compte1, compte2, etc.
Le constructeur de cette classe initialisera deux attributs d’instance nom et solde,
avec les valeurs par défaut ’Dupont’ et 1000.
Trois autres méthodes seront définies :
• deposer(somme) permettra d’ajouter une certaine somme au solde ;
• retirer(somme) permettra de retirer une certaine somme du solde ;
• une méthode pour afficher le nom du titulaire et le solde de son compte.
"""


class CompteBancaire:
    def __init__(self, nom="DUPONT", solde=1000):
        self.nom = nom
        self.solde = solde

    def deposer(self, somme):
        if somme > 0:
            self.solde += somme

    def retirer(self, somme):
        """
        Retire la somme du solde.
        :param somme: Un entier positif.
        """
        if somme > 0:
            self.solde -= somme

    def __str__(self):
        return f"nom : {self.nom}\nsolde : {self.solde}"


compte_bancaire = CompteBancaire("BIDOLET", 1500)
compte_bancaire.deposer(1000)
compte_bancaire.retirer(1000)
print(compte_bancaire)
