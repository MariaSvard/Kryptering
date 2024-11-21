## ta ett enkelt meddelade och kryptera för att sedan dekryptera

from cryptography.fernet import Fernet

with open("secret.key", "rb") as file:
    key = file.read()

cipher_suite = Fernet(key) # objekt för att krytera

message = "Här är mitt hemliga meddelande".encode() # gör om till binary
cipher_text = cipher_suite.encrypt(message) # vad vi vill kryptera
print(f"Ciphertext: {cipher_text}")

with open("encrypted.enc", "wb") as file:
    file.write(cipher_text)

# Nu har vi tagit ett meddelande, skapat en nyckel och krypterat #

# dekryptering

with open("encrypted.enc", "rb") as file:
    encrypted_message = file.read()

plain_text = cipher_suite.decrypt(encrypted_message)
print(f"Dekrypterad text: {plain_text.decode()}")

# print(f"Nyckel laddad: {key}")