import sqlite3
import os

#Take all informations of the database
def getDB(db_name:str)->dict:
  dic = {}
  if not os.path.exists("data/"+db_name+".db"):
    print("No data base named "+db_name)
    return dic
  else:
    conn = sqlite3.connect("data/"+db_name+".db")
    curs = conn.cursor()

    curs.execute("SELECT * FROM key_table")
    rows = curs.fetchall()
    for row in rows:
      dic[f"{row[1]}"] = f"{row[2]}"

    conn.close()
    return dic  


#Add an element in the database
def addToDB(db_name:str, key,value:str):
  if not os.path.exists("data/"+db_name+".db"):
    print("No table named",db_name,"found.")
    return
  conn = sqlite3.connect("data/"+db_name+".db")
  cursor = conn.cursor()

  cursor.execute("INSERT INTO key_table (key,value) VALUES(?,?)",(key,value))

  print("Adding element succed!")

  conn.commit()
  conn.close()


#Delete a specified element in the database
def deleteKey(db_name:str, key:str):
  if not os.path.exists("data/"+db_name+".db"):
    print(f"No table named "+db_name+" found at data/"+db_name+".db")
    return
  
  conn = sqlite3.connect("data/"+db_name+".db")
  cursor = conn.cursor()

  cursor.execute("SELECT * FROM key_table WHERE key = ?", (key,))
  row = cursor.fetchone()

  if row:
    cursor.execute("DELETE FROM key_table WHERE key = ?", (key,))
    conn.commit()
    print(f"{row[1]} deleted.")
  else :
    print(f"No element corresponding to {row[1]}")  

#Create a new database
def createDB(db_name:str)->bool:
  if not os.path.exists("data/"+db_name+".db"):
    f = open("data/"+db_name+".db","w")
    f.close()
    
    conn = sqlite3.connect("data/"+db_name+".db")
    curs = conn.cursor()
    curs.execute('''
    CREATE TABLE IF NOT EXISTS key_table(
                id INTEGER PRIMARY KEY,
                key TEXT NOT NULL,
                value TEXT NOT NULL
                )'''
    )
    print(db_name,"as been created.")
    conn.close()
    return False
  else:
    print(db_name+" already exist :)")
    return True  