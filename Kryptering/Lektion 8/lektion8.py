# hur man använder filhanteringen
# symmetrisk kryptografi
# fernet

## börja med att importera standardbiblioteket Fernet ##

from cryptography.fernet import Fernet
# nu kan vi anropa klassen och alla tillbehör som finns

## Generera en nyckel ##

# skapa/definera en variabel
# anropa klassen från standardbiblioteket
# key = Fernet.generate_key() # genererar en symmetrisk nyckel, bytes

# print(f"Generate key: {key.decode()}") # anropar nyckeln, dekrypterar

# spara nyckeln i en fil
# ge funktionen argument så att programmet vet vad som ska göras
# spara till en fil genom att öppna en fil
# with open("secret.key", "wb") as key_file: # key_file definerar filen
#     key_file.write(key)
# print(f"Key is saved to file 'Secret.key'") # vart den är nerladdad
# secret = nyckeln
# definera vilken fil och hur
# wb att vi vill skriva till filen och vad det är för data, binär data

# varje gång man kör funktionen så kommer man få en ny nyckel

## ladda in den genererade nyckeln ##

# öppna en fil "r" # man vill läsa innehållet
with open("secret.key", "rb") as key_file: # r (read) b(gör om till binär)
    key = key_file.read()
print(f"Key is loaded: {key.decode()}") # istället för att skriva till filen så kommer vi läsa innehållet
# samma som att skriva i terminalen cat.secret.key
# nu har vi inte läst in filen genom att anropa funktionen, utan vi har bara läst filen

## När vi läst in och laddat upp nyckeln ska vi skapa ett objekt ##

# skapa ett class-objekt, ett Fernet-objekt då kan vi manipulera allt som klassen innehåller
# vi skapar ett Fernet-objekt för att kunna kryptera saker
# definera en variabel till ett oblekt som är Fernet-klassen key(den inlästa nyckeln)
cipher_suite = Fernet(key) # skapar en instans till classen Fernet
print("Fernet object is created and ready for encryption")

## Kryptera ett meddelande ##
# definera en variabel med en sträng

message = "This is a string with a secret message".encode() # encode konverterar stängen till bytes
cipher_text = cipher_suite.encrypt(message) # variabeln för att veta vart vi ska förvara texten
# meddelande + nyckel = cipher_text, returnerar en sträng
# cipher_suite innehåller ett objekt från Fernet-classen
# encrypt är från Fernet-classen och tar ett argument som är vårt (message/plaintext) och krypterar
print(f"Encrypted message: {cipher_text}")

# spara texten till en fil:
with open("encrypted_message.enc", "wb") as enc_file: # öppna filen och skriv till den
    enc_file.write(cipher_text) # istället för sectret.key
print("Encrypted message is saved to file 'encrypted_message.enc'")

## dekryptera meddelandet ##

# hänsvisa till filen med meddelandet
with open("encrypted_message.enc", "rb") as enc_file: # läsa filen, binär data
    encrypted_message = enc_file.read() # sparar den krypterade texten
    # texten var ciphertext när vi läste in den men nu ska vi göra den till en plaintext igen
print(f"Encrypted message is loaded: {encrypted_message}")
# dekryptera ciphertexten
# definera en variabel plain_text
plain_text = cipher_suite.decrypt(encrypted_message) # dekryptera decrypt
print(f"Decrypted message: {plain_text.decode()}")

## allt detta bygger man ihop till projektet ##