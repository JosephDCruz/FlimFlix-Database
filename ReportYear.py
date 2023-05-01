from connect import *
import time

def filmsByYear():
     "yearReleased"
    # ( 2022 )
     idfield = input("Enter year of the record to be printed:")

    
  
     cursor.execute(f"SELECT * FROM tblFilms WHERE yearReleased = '{idfield}'")
    
     rows = cursor.fetchall()
     for row in rows:
        print(row)
     print(f"{idfield} inputed to records")
     time.sleep(3)
  
if __name__ == "__main__":
    filmsByYear()
