import sqlite3
import os

def getDB(db_name:str)->dict:
  dic = {}
  if os.path.exists("data/"+db_name+".db") == False:
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
    print("No file",db_name+".db","found.\n","\r"+db_name+".db","as been created.")
    conn.close()
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

def addToDB(db_name:str, key,value:str):
  conn = sqlite3.connect("data/"+db_name+".db")
  cursor = conn.cursor()

  cursor.execute("INSERT INTO key_table (key,value) VALUES(?,?)",(key,value))

  print("Adding element succed!")

  conn.commit()
  conn.close()