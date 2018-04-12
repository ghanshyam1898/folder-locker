from Crypto.Cipher import AES
import base64
import sys
import hashlib
import base64
from tkinter import filedialog
from tkinter import *
import shutil


def encryption(privateinfo):
    block_size = 16
    padding = b'{'
    pad = lambda s: s + (block_size - len(s) % block_size) * padding
    EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
    key = receive_key()
    cipher = AES.new(key)
    encoded = EncodeAES(cipher, privateinfo)
    return encoded


def receive_key():
    key = input("Enter the key : ")
    key = ' '.join(format(ord(x), 'b') for x in key)
    key = key.encode('utf-8')
    key = hashlib.md5(key).hexdigest()
    return key


def encrypt_file(path):
    with open(path, 'rb') as given_file:
        data = given_file.read()
        data = encryption(data)
    with open(path, 'wb') as output_file:
        output_file.write(data)


if __name__ == '__main__':
	root = Tk()
	root.withdraw()
	folder_selected = filedialog.askdirectory(title = "Choose folder to lock")
	print("Please wait....")
	shutil.make_archive(folder_selected, 'zip', folder_selected)

	encrypt_file(folder_selected + ".zip")
	input("\nFile locked successfuly.\n\nIt is saved at : {} \n\nPress enter to finish.".format(folder_selected + ".zip"))