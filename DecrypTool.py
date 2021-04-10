import argparse
import base64
import os
from lib.transbase import (
    toBinary,
    toDecimal,
    toHex,
    toOctal,
    fromBase64,
    toBase64,
)
from lib.RSA.rsa_decryption import(
    RsaDecryptWithPrivKey,
    RsaDecryptWithPubKey,
    dumpKey,
)
from lib.RSA.rsa_encryption import (
    generateKeys,
    generateKeysFromValues,
    encryptInRsa,
)
from lib.RSA.keys_wrapper import generate_pq_from_n_and_p_or_q, generate_keys_from_p_q_e_n, PrivateKey
from lib.substitution import cesar
#from lib.rsa_attack import RSAAttack

def main() :


    parser = argparse.ArgumentParser(description=("Decrypt (almost) Everything !"))

    #Args for cesar
    parser.add_argument('-c','--cesar', help='The sentence to decipher')

    #Args for Transbase
    parser.add_argument('--toDecimal', help='To convert the value in decimal')
    parser.add_argument('--toOctal', help='To convert the value in octal')
    parser.add_argument('--toBinary', help='To convert the value in binary')
    parser.add_argument('--toHex', help='To convert the value in hex')
    parser.add_argument('--from', help='The base that the value come from : "hex", "binary", "octal", "decimal"') 

    #Args for Base64
    parser.add_argument('--fromBase64',help='The sentence to decrypt from base64')
    parser.add_argument('--toBase64',help='The sentence to encrypt in base64')

    #Args for RSA
    parser.add_argument("--toRsa", help="The file that you want to encrypt in Rsa with a public key or private key already created or create et pair of keys")
    parser.add_argument("--privateKey", help="The private key in a file")
    parser.add_argument("--publicKey", help="The public key in a file")
    parser.add_argument("--RsaInFile", help="The flag encrypted in a file")
    parser.add_argument("--dumpKey", help="Dump the key, private or public")
    parser.add_argument("--genKeys", help="Generates a pair of keys",action="store_true")


    args = parser.parse_args()
    args = vars(args)

    banner()
    if args["toDecimal"] is not None and args["from"] is not None:
        toDecimal(args["toDecimal"],args["from"])

    if args["toHex"] is not None and args["from"] is not None:
        toHex(args["toHex"],args["from"])

    if args["toOctal"] is not None and args["from"] is not None:
        toOctal(args["toOctal"],args["from"])
    
    if args["toBinary"] is not None and args["from"] is not None:
        toBinary(args["toBinary"],args["from"])

    if args["cesar"] !=  None:
        cesar(args["cesar"])

    if args["fromBase64"] != None:
        fromBase64(args["base64"])

    if args["toBase64"] != None:
        toBase64(args["toBase64"])

    if args["toRsa"] != None:
        encryptInRsa(args["toRsa"],args["publicKey"],args["privateKey"])
    

    flag = args["RsaInFile"]
    privateK = args["privateKey"]
    publicK = args["publicKey"]
    if flag is not None:
        if privateK is not None:
            RsaDecryptWithPrivKey(flag,privateK)
        if publicK is not None:
            RsaDecryptWithPubKey(flag,publicK)
        else :
            print("You have to specify a privateKey")

    if args["dumpKey"] is not None:
        dumpKey(args["dumpKey"])
    
    if args["genKeys"] is True :
        generateKeys()
    
    #If there is no argument specified : launch the help
    boolean = False
    for i in args:
        if args[i] is not None  :
            boolean = True

    if boolean == False:
        os.system('/usr/bin/python DecrypTool.py -h')

    print("\n\tSee you later ! Keep doing some cryptography and hacking stuff\n\n")

def banner() :
    print("""\t
\t\t  ____                           _____           _ 
\t\t |  _ \  ___  ___ _ __ _   _ _ _|_   _|__   ___ | |
\t\t | | | |/ _ \/ __| '__| | | | '_ \| |/ _ \ / _ \| |
\t\t | |_| |  __/ (__| |  | |_| | |_) | | (_) | (_) | |
\t\t |____/ \___|\___|_|   \__, | .__/|_|\___/ \___/|_|
\t\t                       |___/|_|                    
    """)
    print('\n\t\t',"Welcome to DecrypTool, let's decrypt something !\n\n\n")


if __name__ == '__main__' :
    main()

