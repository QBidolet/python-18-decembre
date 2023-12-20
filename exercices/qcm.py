"""
Créer un programme Python pour créer un jeu de QCM.
Vous devez poser des questions à l'utilisateur, il doit y répondre par a/b/c/d.
Une seule réponse par question.
A la fin, vous affichez son score.

Je veux pouvoir ajouter des questions au QCM le plus simplement possible.

Faites attention à bien choisir le type agrégé qui convient pour mémoriser les questions/réponses.

Par exemple :
Bienvenue dans le QCM.
Q1. Un set peut il contenir des valeurs dupliquées ?
a) Vraie
b) Fausse
c) Partiellement vraie
d) Autre

>> b

[...]

Score : 1/3
"""
# Etape 1 : Initialisation des variables
question_1 = """
Q1. Un set peut il contenir des valeurs dupliquées ?
a) Vraie
b) Fausse
c) Partiellement vraie
d) Autre
"""

question_2 = "Comment ... ?"

questions = {
    question_1: "a",
    question_2: "b"
}

# Etape 2 : Déroulement du QCM.
score = 0
print("Bienvenue dans le QCM.")
for question, valeur in questions.items():
    print(question)
    # Obtenir la réponse utilisateur
    user_input = input("Tapez votre réponse (a/b/c/d).\n")
    # Vérifier si la réponse correspond à la valeur de la question
    if user_input == valeur:
        print("Bonne réponse !")
        # Si la réponse est bonne, incrémenter le score.
        score += 1
    else:
        print("Mauvaise réponse !")

# Etape 3 : Affichage du score
print(f"Votre score: {score}/{len(questions)}")