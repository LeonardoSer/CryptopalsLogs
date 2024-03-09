#!/usr/bin/env python3

import sys
import codecs

def xor_two_str(str1,str2):
    str1 = int(str1, base=16)
    str2 = int(str2, base=16)
    return hex(str1 ^ str2)[2:]

buff1 = []
buff2 = []

print("\nIl programma effettua lo xor tra due stringhe esadecimali della stessa misura", "\n")

if(len(sys.argv)==2):
    print("ERR: input non valido, inserisci due stringhe valide")
    exit(0)
elif(len(sys.argv)==1):
    buff1=input("inserisci la prima stringa: ")
    buff2=input("inserisci la chiave esadecimale: ")

if(len(buff1)!=len(buff2) or len(sys.argv[1])!=len(sys.argv[2])): 
    print("ERR: la lunghezza delle stringhe non coincide")
    exit(0)
    
buff1=sys.argv[1]
buff2=sys.argv[2]

try:
    xor= xor_two_str(buff1, buff2)
except Exception as e:
    print("ERR: ", str(e))
    exit(0)

print("stringa1: ", buff1)
print("stringa2: ", buff2)
print()
print("lo xor è: ", xor)
print("in ascii è: ", codecs.decode(xor, "hex").decode("utf-8"))


