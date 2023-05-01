import Read
import AddFilm
import Update
import Delete
import ReportGenre
import ReportRatings
import ReportYear



def menuOptions():
    options = 0
    

    # concept of iteration in python: while loop
    'while 0 not in ["1","2","3","4","5"]'
    while options not in ["1","2","3","4","5","6"]:
        print("filmflix Menu Options\nEnter:\n1. Print.\n2. Add.\n3. Update.\n4. Delete.\n5. Reports\n6. Exit.")

        # re-assign value a new value(ser input) to the options variable
        options = input("Enter an option from the filmflix menu choices above: ")
        # concept of selection 
        if options not in ["1","2","3","4","5"]: 
            print(f"{options} is not a valid choice! from the flimflix menu")
          
    
    return options
def reportSubMenu():
    reportChoice = 0

    # concept of iteration in python: while loop
    while reportChoice not in ["1", "2", "3"]:
        print("filmflix Reports Submenu\nEnter:\n1. List all movies.\n2. List movies by genre.\n3. List movies by year.\n4. Return to main menu.")

        # re-assign value a new value(ser input) to the options variable
        reportChoice = input("Enter an option from the filmflix report submenu choices above: ")
        
        # concept of selection 
        if reportChoice not in ["1", "2", "3", "4"]: 
            print(f"{reportChoice} is not a valid choice from the filmflix report submenu.")
          
        if reportChoice == "1":
            ReportGenre.filmsByGenre()
        elif reportChoice == "2":
            ReportYear.filmsByYear()
        elif reportChoice == "3":
            ReportRatings.filmsByRating()
        elif reportChoice == "4":
            return
        
mainProgram = True
while mainProgram:
    menuChoice = menuOptions()

    if menuChoice == "1":
        Read.read()
    elif menuChoice == "2":
        AddFilm.insertFilms()
    elif menuChoice == "3":
        Update.update()
    elif menuChoice == "4":
        Delete.delete()
    elif menuChoice == "5":
        reportSubMenu()
    
    else:
        mainProgram = False  #assign mainProgra a boolean False variable to exit the while loop
input("Press Enter to quit the application")

  


