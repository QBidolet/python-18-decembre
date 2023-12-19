"""
Un programme qui demande à l'utilisateur de saisir des noms de chat.
Le programme doit s'arrêter quand l'utilisateur le veut.
Ensuite, le programme doit afficher les noms de chat dans l'ordre saisie.

BONUS :
Afficher le numéro du chat avec son nom lors de l'affichage.
Ne pas pouvoir saisir deux fois le même nom de chat.
"""

# Initialisation des variables
chats = []
reponse = ""
mots_stop = ["stop", "exit", "exit()", "non", "quitter"]

# Boucle while car indéfini.
while True:
    # Obtenir la valeur
    reponse = input("Veuillez entrer un nom de chat.\n")

    reponse = reponse.lower().strip()
    if reponse in mots_stop:
        break

    # Nettoyer la saisie
    reponse = reponse.capitalize()

    # Est-ce qu'on peut l'ajouter ?
    if reponse != "" and reponse not in chats:
        chats.append(reponse)
    else:
        print("Vous avez déjà mis ce nom de chat.")

    # Continuer ?
    # reponse = input("Voulez-vous continuer ?\n")
    # reponse = reponse.lower()

# Gestion de l'affichage
for indice, chat in enumerate(chats):
    print(f"Chat n°{indice + 1}: {chat}.")

# Solution alternative sans enumerate.
# numero_chat = 1
# for chat in chats:
#     print(f"Chat n°{numero_chat}: {chat}.")
#     numero_chat += 1