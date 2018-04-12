from tkinter import filedialog
from tkinter import *
import shutil
from Crypto.Cipher import AES
import base64
import sys
import hashlib
import base64
import zipfile
import os


def decryption(data):
    padding = b'{'
    DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(padding)
    key = receive_key()
    cipher = AES.new(key)
    decoded = DecodeAES(cipher, data)
    return decoded


def receive_key():
    key = input("Enter the key : ")
    key = ' '.join(format(ord(x), 'b') for x in key)
    key = key.encode('utf-8')
    key = hashlib.md5(key).hexdigest()
    return key

def test_valid_zip(data):
    temp_file = "tempo4987oewrt9879kjh34.zip"
    with open(temp_file, 'wb') as output_file:
        output_file.write(data)
    try:
        zip1=zipfile.ZipFile(temp_file)
        return True

    except zipfile.BadZipFile as e:
        with open('log.txt', 'w') as log_file:
            log_file.write(str(e))

        print("\nIncorrect password.\n\n")
        return False

    except Exception as e:
        input("Some error occurred. Log recorded in log file. Press enter to exit.")
        with open('log.txt', 'w') as log_file:
            log_file.write(str(e))
            exit(0)

    finally:
        os.remove(temp_file)

def decrypt_file(path):
    with open(path, 'rb') as given_file:
        data = given_file.read()

    while True:
        temp_data = decryption(data)
        if test_valid_zip(temp_data) is True:
            data = temp_data
            break

    with open(path, 'wb') as output_file:
        output_file.write(data)


if __name__ == '__main__':
    root = Tk()
    root.withdraw()
    file_selected = root.filename =  filedialog.askopenfilename(title = "Choose file to unlock",
                                                                filetypes=(
                                                                ("Zip File", "*.zip"),

                                                                ))
    print("Please wait....")
    decrypt_file(file_selected)
    input("\nFile unlocked successfuly.\n\nIt is saved at : {} \n\nPress enter to finish.".format(file_selected))
