import base64
from scripts.crypto import *
from scripts.db_handler import *
from getpass import getpass
import os
import pyperclip

# Function to clear system window
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Ask if the user wants to quit
def Leave() -> str:
    return input("Quit (Q) ?")  

def set_environment_variable(variable_name: str, value: str, path: str):
    try:
        # Définir la variable d'environnement pour le processus courant
        os.environ[variable_name] = value
        
        # Vérifier si le chemin du répertoire existe, sinon le créer
        if not os.path.exists(path):
            os.makedirs(path)
        
        # Ajouter l'extension .env au chemin et écrire dans le fichier
        env_file_path = os.path.join(path, '.env')
        with open(env_file_path, 'a') as file:
            file.write(f'{variable_name}={value}\n')
        
        print(f'Variable d\'environnement {variable_name} définie avec la valeur {value} et enregistrée dans {env_file_path}')
    
    except FileNotFoundError:
        print(f'Erreur : Le chemin spécifié "{path}" est introuvable.')
    
    except PermissionError:
        print(f'Erreur : Permission refusée pour écrire dans le fichier "{env_file_path}".')
    
    except OSError as e:
        # Capturer d'autres erreurs d'entrée/sortie
        print(f'Erreur d\'entrée/sortie : {e}')

clear()
print("======== SAFE KEY ========\n")
password = getpass("Master Password : ")

# Main process
option = ""
while option != "Q":
    clear()
    print("========== MENU ==========\n")
    print('''1 : How to use
2 : Change password
3 : Keys view
4 : Add a Key
5 : Delete a key
6 : Create a key table
7 : Delete a key table 
8 : Set as env variable
9 : Copy in clipboard                           
Q : Quit
''')
  
    option = input("Choice : ")
    if option == "2":  # Changing password/Decrypt key
        clear()
        print("======== SAFE KEY ========\n")
        password = getpass("Master Password : ")

    elif option == "3":  # Show all decrypted keys with the password
        clear()
        print("======== KEY VIEW ========\n")
        if (keys := getDB(input("Enter the data base name : "))) == {}:
            option = input("No database found. Quit (Q) ? "); continue

        for key in keys:
            key_bytes = base64.b64decode(key)  # Assuming key is stored as base64
            value_bytes = base64.b64decode(keys[key])  # Assuming values are stored as base64
            try:
                decrypted_key = decryptData(password, key_bytes)
                decrypted_value = decryptData(password, value_bytes)
                print(f"{decrypted_key.decode()} | {decrypted_value.decode()}")
            except ValueError as e:
                print(f"Error decrypting key/value: {e}")
        option = Leave()

    elif option == "4":  # Add a key to database, encrypted with password
        clear()
        print("======== ADD KEY ========\n")
        db_name = input("Enter the database name : ")
        key_name = encryptData(password, bytes(input("Key name : "), 'utf-8'))
        key_value = encryptData(password, bytes(input("Key value : "), 'utf-8'))
        # Store as base64
        addKey(db_name, base64.b64encode(key_name).decode('utf-8'), base64.b64encode(key_value).decode('utf-8'))
        option = Leave()

    elif option == "5":  # Delete a key from database
        clear()
        print("======= DELETE KEY =======\n")
        db_name = input("Enter the database name : ")
        key_value = input("Value of the key to delete : ")  # Prendre la valeur de la clé à supprimer
        deleteKey(db_name, key_value, password)  # Passer le mot de passe à la fonction de suppression
        option = Leave()

    elif option == "6":  # Create a new table
        clear()
        print("======= NEW TABLE =======\n")
        db_name = input("Enter the database name : ")
        createDB(db_name)
        option = Leave()

    elif option == "7":
        clear()
        print("======= DEL TABLE =======\n")
        db_name = input("Enter the database name : ")
        if os.path.exists("data/"+db_name+".db"):
            os.remove("data/"+db_name+".db")
            print(db_name,"as been deleted.")
            option = Leave()
        else:
            print("No database named",db_name,"found.")
            option = Leave()  

    elif option == "8":
        clear()
        print("======= SET ENV =======\n")
        db_name = input("Enter the database name : ")
        key_name = input("Enter key name : ")
        value = takeKeyValue(db_name,key_name,password)
        path = input("Enter the absolut path to set the key : ")
        if value == "":
            print("No corresponding value find in database.")
            option = Leave()
        else:
            set_environment_variable(key_name,value,path)
            if input("Paste in clipboard (Y) ? ") == "Y": pyperclip.copy(value)
            option = Leave()                   


    elif option == "9":
        clear()
        print("======== COPY ========\n")
        db_name = input("Enter the database name : ")
        key_name = input("Enter key name : ")
        value = takeKeyValue(db_name,key_name,password)
        if value == "":
            print("No corresponding value find in database.")
            option = Leave()
        else:
            print("Value : "+value)
            if input("Paste in clipboard (Y) ? ") == "Y": pyperclip.copy(value)
            option = Leave()


    elif option == "1":
        clear()
        print("======= USING =======\n")
        print('''
WARNING : First of all, the password given is your encryption key, donc't forget it ! We can't help you to recover it ;)

This project help you to manage your keys or password and allow you to set them as an environment variable.

KEYS:
All keys are saved in a database, you could find them in ./SAFEKEY/data/file.db
They are encrypted so nobody could see them, but you have to remember the Master Password.

CRYPTOGRAPHY
When you save a new key, the only way to decrypt it, is with 
the password that you used when you saved it
                                                                                                                                                             
PORTABILITY
Save your crypted files(.db) in a cloud like google drive and paste them in ./SAFEKEY/data/

PATH
We highly recommand to set this program in User/your_user_name/ directory.
With this path, the programm could acces to all projects in User/ to set env variable with : 
program ask path : ../Your/Path/To/Your/Project/                                                                                             
''')        
        option == Leave()