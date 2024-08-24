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
Q : Quit
Choice : ''')
  
  if option == "1":
    clear()
    getDB(input('''
      DB management
Enter the name of the table/file : '''))
    option = input("Leave ? ")
  
  elif option == "2":
    clear()
    addToDB(input("DB : "), input("key : "),input("value : "))
    option = input("Leave ? ")

  elif option == "3":
    clear()   