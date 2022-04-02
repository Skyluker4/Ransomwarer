from os import urandom
from Crypto.Cipher import AES
import os

# Get home directory
home_path = os.path.expanduser('~')
home_path = "/home/luke/Downloads/HackathonSpring2022/Ransomwarer/test/"

# For Generating cipher text
secret_key = b"HotzFellas000000"
iv = b"HotzFellas000000"
obj = AES.new(secret_key, AES.MODE_CBC, iv)

# Encrypt the message
message = 'Lorem Ipsum text'
message_bytes = message.encode('utf-8')
print('Original message is: ', message_bytes.decode('utf-8'))
encrypted_text = obj.encrypt(message_bytes)
print('The encrypted text', encrypted_text)

# Decrypt the message
rev_obj = AES.new(secret_key, AES.MODE_CBC, iv)
decrypted_text = rev_obj.decrypt(encrypted_text)
print('The decrypted text', decrypted_text.decode('utf-8'))
