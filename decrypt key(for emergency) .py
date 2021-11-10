from cryptography.fernet import Fernet

keY = b'gdOEYoJxCrjLlv1u6NFAr9SSmtezinvXVmoYl_e85_g='

f = Fernet(keY)
with open('key.key', "rb") as file :
    # read the encrypted data
    encrypted_data = file.read()
# decrypt data
decrypted_data = f.decrypt(encrypted_data)
# write the original file
with open('key.key', "wb") as file :
    file.write(decrypted_data)