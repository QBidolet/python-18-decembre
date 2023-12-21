from tkinter import *
import sqlite3


def create_database():
    connection = sqlite3.connect('base.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS contacts(nom TEXT, telephone TEXT)")
    connection.commit()
    cursor.close()
    connection.close()
    # Si vous ne connaissez pas le SQL
    # vous pouvez utiliser des ORM comme SQLAlchemy


def inserer():
    connection = sqlite3.connect('base.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO contacts VALUES (?, ?)", (var_nom.get(), var_telephone.get()))
    connection.commit()
    cursor.close()
    connection.close()
    print("Insertion terminée")


def afficher():
    connection = sqlite3.connect('base.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM contacts;")
    for element in cursor.fetchall():
        print(element)
        
    connection.commit()
    cursor.close()
    connection.close()


def init():
    fenetre = Tk()
    fenetre.geometry("410x450")
    fenetre.title("Formulaire")
    fenetre.configure(background="powder blue")

    # Créer des widgets
    label_nom = Label(fenetre, text="Nom :")
    label_nom.place(x=0, y=0)

    label_telephone = Label(fenetre, text="Téléphone :")
    label_telephone.place(x=0, y=30)

    global var_nom, var_telephone
    var_nom = StringVar()
    var_telephone = StringVar()

    entry_nom = Entry(fenetre, width=20, textvariable=var_nom)
    entry_nom.place(x=80, y=0)

    entry_telephone = Entry(fenetre, width=20, textvariable=var_telephone)
    entry_telephone.place(x=80, y=30)

    # création des boutons
    bouton_inserer = Button(fenetre, text="Insérer", command=inserer)
    bouton_afficher = Button(fenetre, text="Afficher", command=afficher)

    bouton_inserer.place(x=80, y=100)
    bouton_afficher.place(x=150, y=100)

    fenetre.mainloop()


if __name__ == "__main__":
    create_database()
    init()
