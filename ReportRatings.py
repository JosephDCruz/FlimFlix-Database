from connect import *
import time

def filmsByRating():

    valid_ratings = "PG,R,G"
    
    idfield = input("Enter rating of the record to be printed:")

    if idfield not in valid_ratings:
        print(f"Invalid rating! Valid ratings are: {valid_ratings}")
        return
  
    cursor.execute(f"SELECT * FROM tblFilms WHERE rating = '{idfield}'")
    
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    print(f"{idfield} inputed to records")
    time.sleep(3)
  
if __name__ == "__main__":
    filmsByRating()
