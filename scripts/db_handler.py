import base64
from scripts.crypto import decryptData
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
def addKey(db_name:str, key,value:str):
  if not os.path.exists("data/"+db_name+".db"):
    print("No table named",db_name,"found.")
    return
  conn = sqlite3.connect("data/"+db_name+".db")
  cursor = conn.cursor()

  cursor.execute("INSERT INTO key_table (key,value) VALUES(?,?)",(key,value))

  print("Adding element succed!")

  conn.commit()
  conn.close()


def deleteKey(db_name: str, key_value: str, password: str):
    if not os.path.exists("data/"+db_name+".db"):
       print("No "+db_name+" table found.")
       return

    conn = sqlite3.connect("data/"+db_name+".db")
    cursor = conn.cursor()

    key_value_bytes = key_value.encode('utf-8')
    encoded_key_value = base64.b64encode(key_value_bytes).decode('utf-8')

    cursor.execute("SELECT id, key, value FROM key_table")
    rows = cursor.fetchall()
    
    keys_to_delete = []

    for row in rows:
        id, encrypted_key_name, _ = row
        try:
            decrypted_key_name = decryptData(password, base64.b64decode(encrypted_key_name))
            if decrypted_key_name.decode('utf-8') == key_value:
                keys_to_delete.append(id)
        except ValueError:
            print(f"Failed to decrypt value for key with id {id}")

    if not keys_to_delete:
        print(f"No element corresponding to {key_value}")
    else:
        cursor.executemany("DELETE FROM key_table WHERE id = ?", [(id,) for id in keys_to_delete])
        conn.commit()
        print(f"Keys corresponding to {key_value} deleted successfully.")
    
    conn.close() 


def takeKeyValue(db_name, key, password:str)->str:
  if not os.path.exists("data/"+db_name+".db"):
       print("No "+db_name+" table found.")
       return ""
  conn = sqlite3.connect("data/"+db_name+".db")
  cursor = conn.cursor()

  cursor.execute("SELECT id, key, value FROM key_table")
  rows = cursor.fetchall()
  for row in rows:
      id, encrypted_key_name, value = row
      try:
          decrypted_key_name = decryptData(password, base64.b64decode(encrypted_key_name))
          if decrypted_key_name.decode('utf-8') == key:
              conn.close()
              return decryptData(password, base64.b64decode(value)).decode('utf-8')
      except ValueError:
          print(f"Failed to decrypt value for key with id {id}")
  conn.close()
  return ""  


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