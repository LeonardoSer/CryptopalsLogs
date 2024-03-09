#!/usr/bin/env python3

import sys
import codecs
import binascii 

def xor_all_hex(str):
    if((len(str)%2)!=0):
        print("la stringa è di lunghezza dispari")
        return 0
    ct = binascii.unhexlify(str)     
    pt=""
    for key in range(256):
        for c in ct:
            pt+=(chr(key^c))
        if(pt[:-1].isprintable()):
            print(chr(key), ": ", end='')
            print(pt)
        pt = ""
    return 0            

buff=[]

if(len(sys.argv)==1):
    buff=input("inserisci la stringa: ")
else:
    buff=sys.argv[1]

try:
    xor_all_hex(buff)
except Exception as e:
    print("ERR: ", str(e))
    exit(0)

















