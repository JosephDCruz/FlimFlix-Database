from connect import *
import time

def filmsByGenre():

    valid_genres = "Action,Comedy,Test,Animation,Fantasy,Crime,Horror,Thriller"
    
    idfield = input("Enter genre of the record to be printed:")

    if idfield not in valid_genres:
        print(f"Invalid genre! Valid genres are: {valid_genres}")
        return
  
    cursor.execute(f"SELECT * FROM tblFilms WHERE Genre = '{idfield}'")
    
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    print(f"{idfield} inputed to records")
    time.sleep(3)
  
if __name__ == "__main__":
    filmsByGenre()
