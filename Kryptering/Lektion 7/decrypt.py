## ta ett enkelt meddelade och kryptera för att sedan dekryptera

from cryptography.fernet import Fernet

with open("secret.key", "rb") as file:
    key = file.read()

cipher_suite = Fernet(key) # objekt för att krytera

# dekryptering

with open("encrypted.enc", "rb") as file:
    encrypted_message = file.read()

plain_text = cipher_suite.decrypt(encrypted_message)
print(f"Dekrypterad text: {plain_text.decode()}")