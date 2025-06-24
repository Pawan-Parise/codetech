from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

def pad(data):
    return data + b"\0" * (16 - len(data) % 16)

def encrypt_file(filename, key):
    cipher = AES.new(key, AES.MODE_CBC)
    with open(filename, 'rb') as f:
        data = pad(f.read())
    iv = cipher.iv
    encrypted = cipher.encrypt(data)
    with open(filename + ".enc", 'wb') as f:
        f.write(iv + encrypted)
    print("✅ File encrypted.")

def decrypt_file(filename, key):
    with open(filename, 'rb') as f:
        iv = f.read(16)
        encrypted = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypted = cipher.decrypt(encrypted).rstrip(b"\0")
    with open(filename.replace(".enc", ".dec"), 'wb') as f:
        f.write(decrypted)
    print("✅ File decrypted.")

key = get_random_bytes(32)  # AES-256 key
file_to_encrypt = input("Enter filename to encrypt: ")
encrypt_file(file_to_encrypt, key)

# To decrypt, you can later call:
# decrypt_file(file_to_encrypt + ".enc", key)
