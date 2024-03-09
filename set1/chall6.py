#!/usr/bin/env python3 
from base64 import b64decode

def hammingDistance(str1, str2):
    hammingDist = 0
    for b1, b2 in zip(str1, str2):
        xor = b1 ^ b2
        hammingDist += sum([1 for bit in bin(xor) if bit=='1'])
    return hammingDist

def englishScore(byteEnglishText):
    
    byteEnglishText = byteEnglishText.lower()
    character_frequencies = {
         'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
         'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
         'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
         'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
         'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
         'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
         'y': .01974, 'z': .00074, ' ': .13000
         }

    return sum([character_frequencies.get(chr(b), 0) for b in byteEnglishText])
 

def singleCharXor(byteCiphertext, char):
    bytePlaintext = b'' 
    for b in byteCiphertext:
        bytePlaintext += bytes([b^char])
    return bytePlaintext


def bruteForceSingleCharXor(ciphertext):
    potentialMsgs = []
    score = ""
    for key in range(256):
        msg = singleCharXor(ciphertext, key)
        score = englishScore(msg)
           
        data = {'key': key,
                'message': msg,
                'score': score
                }
        potentialMsgs.append(data)
    return sorted(potentialMsgs, key=lambda x: x['score'], reverse=True)[0] 

def repeatingKeyXor(byteCiphertext, key):
    bytePlaintext = b''
    i=0
    for b in byteCiphertext:
        bytePlaintext += bytes([b^key[i]])
        i+=1
        if(i==len(key)):
                i = 0
    return bytePlaintext

def repeatingXorBreaker(ciphertext):
    avgDistances = []
    key = b'' 
    plaintext = b''
    for keyLen in range(2, 41):
        distances = []
        chunks = [ciphertext[i:i+keyLen] for i in range(0, len(ciphertext), keyLen)]

        for i in range(0, len(chunks)-1, 2):
            distances.append((hammingDistance(chunks[i], chunks[i+1])/keyLen))        
        avgDistances.append({
            'keyLen': keyLen,
            'avgDist': sum(distances)/len(distances)
            })
    possibleKeyLen = sorted(avgDistances, key=lambda x : x['avgDist'])[0]['keyLen']
    for i in range(possibleKeyLen):
        block = b''
        for j in range(i, len(ciphertext), possibleKeyLen):
            block += bytes([ciphertext[j]])
        key += bytes([bruteForceSingleCharXor(block)['key']])
    plaintext = repeatingKeyXor(ciphertext, key)
    return  {'plaintext': plaintext, 'key': key}

with open("chall6_ct.txt", 'r') as infile:
    ciphertext = b64decode(infile.read())

brokenCT = repeatingXorBreaker(ciphertext)
print("\nkey: ", brokenCT['key'])
print("\nPLAINTEXT:\n\n", brokenCT['plaintext'].decode())
