# Import Sqlite3
import sqlite3 as sql
# Import de PrettyTable (affichage du tableau dans la console)
from prettytable import from_db_cursor

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
"""
