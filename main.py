from db_handler import *
import os

option = ""

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

while option != "Q":
  clear()
  option = input('''
      DB management
1 : Show the keys
2 : Add a new key
3 : Delete a key
4 : Create new data base                 
Q : Quit
Choice : ''')
  
  if option == "1":
    clear()
    table = getDB(input('''
      DB management
Enter the name of the table/file : '''))
    print("")
    for row in table:
      print("key : "+row," | ","value : "+table[row])
    option = input("Leave ? ")
  
  elif option == "2":
    clear()
    print("\n     DB Management")
    addToDB(input("DB : "), input("key : "),input("value : "))
    option = input("Leave ? ")

  elif option == "3":
    clear()
    print("\n     DB Management")
    deleteKey(input("DB : "),input("Wich key would you delete ? "))
    option = input("Leave ? ")

  elif option == "Q":
    clear()
    print('''
      DB management
GOOD BYE!''')
    break 

  elif option == "4":
    clear()
    print('''
      DB management
''')
    createDB(input("Enter the name of the new DB : "))
    option = input("Leave ? ")  