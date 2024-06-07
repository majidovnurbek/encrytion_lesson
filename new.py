from cryptography.fernet import Fernet
message = "admin"
key = Fernet.generate_key()
fernet = Fernet(key)
encMessage = fernet.encrypt(message.encode())

print(message)
print(encMessage)