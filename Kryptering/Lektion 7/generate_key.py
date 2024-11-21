from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(f"Genererad nyckel: {key.decode()}")

# nyckeln genereras i binär data #
# data = b"" # binär data

with open("secret.key", "wb") as file: # "wb" för binär fil
    file.write(key)