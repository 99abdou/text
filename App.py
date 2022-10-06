# app.py
import sqlite3

print("Application de Gestion de contacte avec Python et Sqlite3")

with sqlite3.connect("contact.db") as connection:
    cursor = connection.cursor()

def create_table():
    cursor.execute(
        "CREATE TABLE contacte (id INTEGER PRIMARY KEY AUTOINCREMENT,nomComplet TEXT, email TEXT, telephone TEXT)")
    
    
    connection.commit()
  
def ajouter_contacte():    
    cursor.execute(
        "INSERT INTO contacte(nomComplet, email, telephone) VALUES('Abdou Santos', 'abdou@email.com', '772588525')")
    cursor.execute(
        "INSERT INTO contacte(nomComplet, email, telephone) VALUES('Aziz Ba', 'Aziz@email.com', '762588525')")
    cursor.execute(
        "INSERT INTO contacte(nomComplet, email, telephone) VALUES('Aliou fall', 'Aliou@email.com', '702588525')")
        
    connection.commit()

def afficher_les_contacte():    
    rows = cursor.execute("SELECT * FROM contacte").fetchall()
    print(rows)
    
    
def affiche_un_contacte():
    row = cursor.execute(
        "SELECT * FROM contacte WHERE telephone = 702588525").fetchall()
    print(row)
    

def supprimer_un_contacte():
    telephone = 772588525
    cursor.execute(
        "DELETE FROM contacte WHERE telephone = ?",
        (telephone,)
        )
    connection.commit()
    
    
def modifier_un_contacte():
    nouveau_contacte = "752588599"
    ancien_contacte = "702588525"
    cursor.execute(
        "UPDATE contacte SET telephone = ? WHERE telephone = ?",
        (nouveau_contacte, ancien_contacte)
        )
    connection.commit()
    


    