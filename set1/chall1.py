#!/usr/bin/env python3

import sys
import codecs

print("\nIl programma effettua un cambio di base da esadecimale a base64 della stringa in input\n")
if len(sys.argv)!=2:
    ct = input("inserisci il cyphertext esadecimale: ")  
else:
    ct = sys.argv[1]

try:
    hexCT = codecs.decode(ct, "hex")
    pt = codecs.encode(hexCT, "base64")
    print("cyphertext originale: ", hexCT.decode("utf-8"), "\n")
    print("in base16: ", ct)
    print("in base64: ", pt.decode("utf-8"))
except Exception as e:
    print("ERR: ", str(e))
    exit(0)








