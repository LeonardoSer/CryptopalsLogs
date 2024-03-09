#!/usr/bin/env python3

import sys
import codecs
import binascii
from array import array

def rep_xor(pt, key):
    ct=""
    while(len(pt)>len(key)):
            key+=key
    if(len(key)>len(pt)):
        key=key[:-(len(key)-len(pt))]
    for i in range(len(pt)):
        ct += chr(ord(pt[i]) ^ ord(key[i]))
    return ct

pt=""
ct=""
key=""

if(len(sys.argv) == 1):
    pt = (input("inserisci il plaintext: "))
    key = (input("inserisci la chiave: "))
elif(len(sys.argv) == 2):
    with open(sys.argv[1]) as file:
        for line in file:
            pt += (line)
    key = (input("inserisci la chiave: "))
else:
    with open(sys.argv[1]) as file:
        for line in file:
            pt += (line)
    with open(sys.argv[2]) as file:
        for line in file:
            key += (line)

print("\nPLAINTEXT: ", pt, end='')
print("CHIAVE: ", key, "\n")

ct = rep_xor(pt, key)
print(ct)
ct = binascii.hexlify(ct.encode())

print("il cyphertext è: ", ct.decode()[:-2])
