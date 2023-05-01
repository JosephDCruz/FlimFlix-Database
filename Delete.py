from connect import *
from Read import*
import time

def delete():
    "filmID, title, yearReleased, rating, duration, genre"
    # (1, 'The Muppets', 2022, 'PG', 116, 'Comedy')

    idfield = input("Enter filmId of the record to be deleted:")

    cursor.execute(f"DELETE from tblFilms WHERE filmID = '{idfield}'")
    conn.commit()

    print(f"{idfield} deleted from tblFilms table")
    time.sleep(3)
if __name__ == "__main__":
    delete()

