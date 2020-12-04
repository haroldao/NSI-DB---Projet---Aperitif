# Import Sqlite3
import sqlite3 as sql
# Import de PrettyTable (affichage du tableau dans la console)
from prettytable import from_db_cursor

CREATE_ARTICLE_TABLE = "CREATE TABLE IF NOT EXISTS Articles(id INTEGER PRIMARY KEY, designation TEXT, prix INTEGER, quantité unitaire TEXT)"
INSERT_ARTICLE = "INSERT INTO Articles (designation, prix, quantité) VALUES (?, ?, ?)"

CREATE_PERSON_TABLE = "CREATE TABLE IF NOT EXISTS Personne(id INTEGER PRIMARY KEY, nom TEXT, prénom TEXT, produit TEXT references Articles(designation))"
INSERT_PERSON = "INSERT INTO Personne (nom, prénom, produit) VALUES (?, ?, ?)"

MENU_PROMPT = """
#=========================================
#Bienvenu sur l'interface NSI Apéritif :
#=========================================
Quelle action souhaitez vous effectuez ? répondre par 1,2,3,4 ou 5:
1 - C - Ajouter un convive, un article.
2 - R - Consulter la liste des articles
3 - U - Modifier la personne apportant tel ou tel article.
4 - D - Supprimer un article ou une personne.
5 - Quitter l'application.

Je veux choisir l'option : """


######################## Application #######################

def create_table():
    connection = sql.connect("aperitif.db")
    cursor = connection.cursor()

    cursor.execute(CREATE_ARTICLE_TABLE)
    cursor.execute(CREATE_PERSON_TABLE)
    connection.commit()
    connection.close()


def add_person(last_name, first_name, product):
    connection = sql.connect("aperitif.db")
    cursor = connection.cursor()

    cursor.execute(INSERT_PERSON, (last_name, first_name, product))
    connection.commit()
    connection.close()


def add_product(product_name, price, quantity):
    connection = sql.connect("aperitif.db")
    cursor = connection.cursor()

    cursor.execute(INSERT_ARTICLE, (product_name, price, quantity))

    connection.commit()
    connection.close()


create_table()


def app():

    while(user_input := input(MENU_PROMPT)) != "5":
        if user_input == "1":
            select = input(
                "Vous souhaitez ajouter un convive ou un article?\nTapez 1 pour un convive. Tapez 2 pour un article ")

            if select == "1":
                last_name = input("Entrer le nom du convive ? : ")
                first_name = input("Entrer le prénom du convive: ")
                product = input("Entrer le nom du produit qu'elle va amener")
                price = input("Quel est le prix du produit")
                quantity = input("Entrez la quantité du produit")

                add_product(product, price, quantity)
                add_person(last_name, first_name, product)

            elif select == "2":
                pass

            else:
                print("Oops outofrange")

        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            print("Oups... 😥... essayez encore !")


app()
