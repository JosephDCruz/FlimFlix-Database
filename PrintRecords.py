# import required modules

import sqlite3 as sql 

conn = sql.connect("Flimflix Database/filmflix.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM tblFilms ")

result = cursor.fetchall()

def printallfilms():
    for row in result:
        print(row)
        print("\n")

if __name__ == "__main__":
    printallfilms()