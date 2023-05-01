from connect import *
from Read import *
import time

def insertFilms():
    # creates an empty list
    films = []

    # ask for user input for Title, yearReleased, rating, duration and Genre
    title = input("Enter film Title:")
    yearReleased = input("Enter film Release Year:")
    rating = input("Enter film Rating:")
    duration = input("Enter film duration:")
    genre = input("Enter film genre:")

    # append data from above to films list
    films.append(title)
    films.append(yearReleased)
    films.append(rating)
    films.append(duration)
    films.append(genre)

    # Insert data from films list into the database in the filmflix table
    cursor.execute("INSERT INTO tblFilms (title, yearReleased, rating, duration, genre) VALUES(?,?,?,?,?)", films)

    conn.commit()
    print(f"{title} added to filmflix table")
    time.sleep(3)
    read() # call read function

if __name__ == "__main__":
    insertFilms()
