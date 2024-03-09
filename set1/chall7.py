#!/usr/bin/env python3

from Crypto.Cipher import AES
from base64 import b64decode

key = "YELLOW SUBMARINE"
cipher = AES.new(key.encode(), AES.MODE_ECB)
with open("chall7_ct.txt") as inFile:    
    ciphertext = b64decode(inFile.read())

plaintext = cipher.decrypt(ciphertext)
print(plaintext)












