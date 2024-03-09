#!/usr/bin/env python3

import sys
import codecs
import binascii

def xor_all_hex(str):    
    if((len(str)%2)!=0):
        print("la stringa è di lunghezza dispari\n")
        return -1 
    ct = binascii.unhexlify(str)
    pt=""
    for key in range(256):
        for c in ct:
            pt+=(chr(key^c))
        if(pt[:-1].isprintable()):
            print("        ", chr(key), ": ", end='')
            print(pt)
        pt = ""
    return 1

def getLine(filePath, index):
    fileLines=[]
    with open(filePath) as file:
        for line in file:
            fileLines.append(line)
    if(index>=len(fileLines)):
        return -1
    return fileLines[index][:-1]

i=0
inRange=1
while(inRange==1):
    curr=getLine("chall4_file.txt", i)
    if(curr!=-1):
        print(i, ": ", curr)
        xor_all_hex(curr)
    else:
       inRange=0
    i=i+1

