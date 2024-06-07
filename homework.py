1-vazifa
from cryptography.fernet import Fernet
message = "admin"
key = Fernet.generate_key()
fernet = Fernet(key)
encMessage = fernet.encrypt(message.encode())

decrypt= fernet.decrypt(encMessage)

print(message)
print(decrypt)



# 2-vazifa
import rsa
(publickey, privatekey) = rsa.newkeys(1024)
message='salom!'.encode('utf8')
ciphertext = rsa.encrypt(message, publickey)
print(ciphertext)

message2 = rsa.decrypt(ciphertext, privatekey)
print(message2)

print(message2.decode('utf8'))





# 3-vazifa
import rsa
(publickey, privatekey) = rsa.newkeys(1024)
data = 'Hello!'.encode('utf8')
signature = rsa.sign(data, privatekey, 'SHA-1')
rsa.verify(data, signature, publickey)


data2 = 'salom'.encode('utf8')
hash = rsa.compute_hash(data2, 'SHA-1')
signature2 = rsa.sign_hash(hash, privatekey, 'SHA-1')

print(signature2)
