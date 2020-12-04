# Import Sqlite3
import sqlite3 as sql
# Import de PrettyTable (affichage du tableau dans la console)
from prettytable import from_db_cursor

CREATE_PERSON_TABLE = "CREATE TABLE Personne(id INTEGER PRIMARY KEY, nom TEXT, prénom TEXT)"
INSERT_PERSON = "INSERT INTO Personne (nom, prenom) VALUES (?, ?)"

CREATE_ARTICLES_TABLE = "CREATE TABLE Articles(id INTEGER PRIMARY KEY, designation TEXT, prix INTEGER, quantité unitaire TEXT)"
INSERT_ARTICLES = "INSERT INTO Articles (designation, prix, quantité unitaire) VALUES (?, ?, ?)"


MENU_PROMPT = """
#=========================================
#Bienvenu sur l'interface NSI Todo Liste :
#=========================================
Quelle action souhaitez vous effectuez ? répondre par 1,2,3,4 ou 5:
1 - C - Ajouter un convive, un article.
2 - R - Consulter la liste des articles
3 - U - Modifier la personne apportant tel ou tel article.
4 - D - Supprimer un article ou une personne.
5 - Quitter l'application.

Je veux choisir l'option : """


######################## Application #######################


def app():

    while(user_input := input(MENU_PROMPT)) != "5":
        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            print("Oups... 😥... essayez encore !")


app()
