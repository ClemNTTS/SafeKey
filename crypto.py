from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.exceptions import InvalidTag

IV = b"FiXeDiv02542"                        #fixed 12b initial vector, custom as you want too

#Create a key with the user password's
def deriveKey(password:str)->bytes:
  salt = b'custom0your7sal1'                #fixed 16bytes salt, custom it as you want
  kdf = PBKDF2HMAC(
      algorithm=hashes.SHA256(),
      length=32,
      salt=salt,
      iterations=100000,
      backend=default_backend()
  )
  return kdf.derive(password.encode())


#Encrypte the following data with the password modified in an hash
def encryptData(password:str, plaintext:bytes)-> bytes:
  key = deriveKey(password)
  iv = IV
  cipher = Cipher(algorithms.AES(key), modes.GCM(iv),backend=default_backend())
  encryptor = cipher.encryptor()
  cipher_text = encryptor.update(plaintext) + encryptor.finalize()
  return cipher_text + encryptor.tag


#Decrypt a text with a password modified in an hash
def decryptData(password:str, ciphertext_and_tag:bytes)->bytes:
  key = deriveKey(password)
  iv = IV
  tag = ciphertext_and_tag[-16:]
  ciphertext = ciphertext_and_tag[:-16]
  cipher = Cipher(algorithms.AES(key), modes.GCM(iv,tag),backend=default_backend())
  decryptor = cipher.decryptor()

  try:
    return decryptor.update(ciphertext)+decryptor.finalize()
  except InvalidTag:
     raise ValueError("Mauvais mdp ou fichier corrompu")


# Exemple d'utilisation
mot_de_passe = input("Mdp : ")
fichier_clair = b"Ceci est le contenu du fichier."

# Chiffrement
fichier_chiffre = encryptData(mot_de_passe, fichier_clair)
print("Fichier chiffré :", fichier_chiffre,"\n")

try:
    fichier_dechiffre = decryptData("petitchat", fichier_chiffre)
    print("Fichier déchiffré :", fichier_dechiffre)
except ValueError as e:
    print(e)

try:
    fichier_dechiffre = decryptData(mot_de_passe, fichier_chiffre)
    print("Fichier déchiffré :", fichier_dechiffre)
except ValueError as e:
    print(e)
