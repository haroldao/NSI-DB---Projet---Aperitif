# Import Sqlite3
import sqlite3 as sql
# Import de PrettyTable (affichage du tableau dans la console)
from prettytable import from_db_cursor

CREATE_ARTICLE_TABLE = "CREATE TABLE IF NOT EXISTS Articles(id INTEGER PRIMARY KEY, designation TEXT, prix INTEGER, quantité unitaire TEXT)"
INSERT_ARTICLE = "INSERT INTO Articles (designation, prix, quantité) VALUES (?, ?, ?)"

CREATE_PERSON_TABLE = "CREATE TABLE IF NOT EXISTS Personne(id INTEGER PRIMARY KEY, nom TEXT, prénom TEXT, produit TEXT references Articles(designation))"
INSERT_PERSON = "INSERT INTO Personne (nom, prénom, produit) VALUES (?, ?, ?)"

'''CREATE TABLE IF NOT EXISTS Personne(id INTEGER PRIMARY KEY, nom TEXT, prénom TEXT, produit TEXT, FOREIGN KEY(produit) REFERENCES Articles(designation))'''


MENU_PROMPT = """
# =========================================
# Bienvenu sur l'interface NSI Apéritif :
# =========================================
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


def show_table(table):
    connection = sql.connect("aperitif.db")
    cursor = connection.cursor()

    query = '''
        SELECT *
        FROM {}'''.format(table)

    cursor.execute(query)
    connection.commit()

    mytable = from_db_cursor(cursor)
    print("La table actuellement ⏬\n", mytable)

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


def get_articles(select):
    connection = sql.connect("aperitif.db")
    cursor = connection.cursor()

    if select == "1":
        query = '''
            SELECT *
            FROM Articles
        '''
        cursor.execute(query)
        mytable = from_db_cursor(cursor)
        print("\n\nTable de la liste complète ⏬\n\n", mytable)

    elif select == "2":
        query_2 = '''
            SELECT Articles.designation, Articles.prix, Articles.quantité, Personne.nom, Personne.prénom
            FROM Articles
            INNER JOIN Personne ON Articles.designation = Personne.produit
        '''

        cursor.execute(query_2)
        mytable_2 = from_db_cursor(cursor)
        print("\n\nTable pour les produits dont on connait le nom de l'acheteur ⏬\n\n", mytable_2)

    elif select == "3":
        pass
    # A faire

    elif select == "4":
        query_4 = '''
            SELECT id, nom, prénom FROM Personne
        '''
        cursor.execute(query_4)
        mytable_4 = from_db_cursor(cursor)
        print("\n\nTable pour savoir la liste des convives ⏬\n\n", mytable_4)

    else:
        pass


def update_buyer(id, last_name, first_name):
    connection = sql.connect("aperitif.db")
    cursor = connection.cursor()
    query = '''
    INNER JOIN Personne ON Articles.designation = Personne.produit
    UPDATE Articles
    SET Personne.nom = '{}'
    WHERE id = {}'''.format(last_name, first_name)

    cursor.execute(query)
    connection.commit()
    connection.close()


def update_quantity():
    pass


def delete_product(id):
    connection = sql.connect("aperitif.db")
    cursor = connection.cursor()

    query = '''
        DELETE
        FROM Articles
        WHERE id = {}
    '''.format(id)

    cursor.execute(query)
    connection.commit()
    connection.close()


def delete_person(id):
    connection = sql.connect("aperitif.db")
    cursor = connection.cursor()

    query = '''
        DELETE
        FROM Personne
        WHERE id = {}'''.format(id)

    cursor.execute(query)
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
                product_name = input("Entrer le nom du produit: ")
                price_product = input(
                    "Entrer le prix du produit (à l'unité): ")
                product_qty = input("Entrer la quantité du produit: ")

                product_buyer_intro = input(
                    "Souhaitez-vous renseignez le nom de l'acheteur ? [Oui / Non]: ")
                add_product(product_name, price_product, product_qty)

                if product_buyer_intro == "Oui":
                    last_name = input("Entrer le nom du convive ? : ")
                    first_name = input("Entrer le prénom du convive: ")
                    add_person(last_name, first_name, product_name)

                elif product_buyer_intro == "Non":
                    add_product(product_name, price_product, product_qty)

            else:
                print("Oops outofrange")

        elif user_input == "2":
            select = input('''Tapez 1 ⏩ si vous souhaitez consulter la liste complète des articles\nTapez 2 ⏩ si vous souhaitez la liste des articles dont l'acheteur est connu\nTapez 3 ⏩ si vous souhaitez la liste des articles qui n'ont pas d'acheteur\nTapez 4 ⏩ si vous souhaitez consulter la liste des convives\n''')

            get_articles(select)

        elif user_input == "3":
            select = input(
                '''Tapez 1 ⏩ si vous souhaitez modifier l"acheteur d'un article\nTapez 2 ⏩ si vous souhaitez modifier la quantité d'un article\n''')

            if select == "1":
                id = int(input("Entrez l'id"))
                last_name = input("Entrer le nom de famille")
                first_name = input("Entrer le prénom")
                update_buyer(id, last_name, first_name)

            elif select == "2":
                update_quantity()

        elif user_input == "4":
            select = input(
                '''Tapez 1 si vous souhaitez supprimer un article\nTapez 2 si vous souhaitez supprimer un convive\n''')

            if select == "1":
                show_table("Articles")
                id = int(
                    input("Enter l'id du produit que vous souhaitez supprimer: "))
                delete_product(id)
                print("\nVotre produit a bien été supprimé 😎")

            elif select == "2":
                show_table("Personne")
                id_2 = int(
                    input("Entrer l'id de la personne que vous souhaitez supprimer: "))
                delete_person(id_2)
                print("\nLe convive a bien été supprimé 😎")
        else:
            print("Oups... 😥... essayez encore !")


app()
