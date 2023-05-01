from connect import *
from Read import*
import time

def update():
    "filmID, title, yearReleased, rating, duration, genre"
    # (1, 'The Muppets', 2022, 'PG', 116, 'Comedy')

    idfield = input("Enter filmId of the record to be updated:")

    fieldName = input("Enter (title or yearReleased or rating or duration or genre) as field name:")

    fieldValue = input(f"Enter the value for the: {fieldName} field: ")

    print(fieldValue)


    fieldValue = "'" + fieldValue + "'"
    print(fieldValue)

    cursor.execute(f"UPDATE tblFilms SET {fieldName} = {fieldValue} WHERE filmID = {idfield}")
    conn.commit() #makes changes permanent
    print(f"Record {idfield} updated in the films table")
    time.sleep(3) #delay for three seconds

    #call/invoke the read songs function from the Read.py file
    read()
if __name__ == "__main__":
    update()




