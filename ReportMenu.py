import ReportGenre
import ReportRatings
import ReportYear
import PrintRecords

# create a function for the songs menu
def reportOptions():
    options = 0 

    # concept of iteration in python: while loop
    'while 0 not in ["1","2","3","4","5"]'
    while options not in ["1","2","3","4","5"]:
        print("Songs Menu Options\nEnter:\n1.Print details of all films  .\n2. Print all films of a particular genre .\n3.Print all films of a particular year .\n4. Print all films of a particular rating.\n5. Exit.")

        # re-assign value a new value(ser input) to the options variable
        options = input("Enter an option from the songs menu choices above: ")
        # concept of selection 
        if options not in ["1","2","3","4","5"]: 
            print(f"{options} is not a valid choice! from the songs menu")

    return options

mainProgram = True # assign mainProgra a boolean True variable
while mainProgram: # same as while True
    mainMenu = reportOptions()# assign menuOptions function to te mainMenu variable
    if mainMenu == "1":
        PrintRecords.printallfilms()
    elif mainMenu == "2":
        ReportGenre.filmsByGenre()
    elif mainMenu == "3":
        ReportYear.filmsByYear()
    elif mainMenu == "4":
        ReportRatings.filmsByRating()
    
    else:
        mainProgram = False  #assign mainProgra a boolean False variable to exit the while loop
input("Press Enter to quit the application")

if __name__ == "__main__":
    reportOptions()