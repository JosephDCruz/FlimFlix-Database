from connect import *

def read():
 cursor.execute ("SELECT * FROM tblFIlms")

 row = cursor.fetchall()
 for record in row:
   
   print(record)
if __name__ == "__main__":
     read()

   
  