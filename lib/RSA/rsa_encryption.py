import os
import base64
from Crypto.PublicKey import RSA
from lib.RSA.keys_wrapper import generate_pq_from_n_and_p_or_q, generate_keys_from_p_q_e_n, PrivateKey

def generateKeysFromValues(n,e,p,q):
    if n and (p or q):
        p, q = generate_pq_from_n_and_p_or_q(n, p, q)
    #publicKey, privateKey = generate_keys_from_p_q_e_n(None, None, e, n)


def generateKeys():
    os.system('openssl genrsa -out privateKey.pem')
    os.system('openssl rsa -in privateKey.pem -pubout -out publicKey.pem')
    print("Don't let anyone see your private key !")

def encryptInRsa(file,publicKey,privateKey):
    if publicKey != None:
        os.system('openssl rsautl -encrypt -in '+file+' -inkey '+publicKey+' -pubin -out ' + file+'.enc')
        print("\nYou have encrypted your file with your public key")

    if privateKey != None:
        os.system('openssl rsautl -encrypt -in '+file+' -inkey '+privateKey+' -out ' + file+'.enc')
        print("You have encrypted your file with your private key")
    else :
        generateKeys()
        os.system('openssl rsautl -encrypt -in '+file+' -inkey publicKey.pem -pubin -out ' + file+'.enc')
        print("\nNow you have 3 files, the public key, the private one and your file encrypted")

