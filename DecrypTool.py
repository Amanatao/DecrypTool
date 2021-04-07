import argparse
import base64
import os
from Crypto.PublicKey import RSA
def main() :


    parser = argparse.ArgumentParser(description=("Decrypt Everything !"))

    #Args for cesar
    parser.add_argument('-c','--cesar', help='The sentence to decipher')

    #Args for Transbase
    parser.add_argument('--toDecimal', help='To convert the value in decimal')
    parser.add_argument('--toOctal', help='To convert the value in octal')
    parser.add_argument('--toBinary', help='To convert the value in binary')
    parser.add_argument('--toHex', help='To convert the value in hex')
    parser.add_argument('--from', help='The base that the value come from : "hex", "binary", "octal", "decimal"') 

    #Args for Base64
    parser.add_argument('--base64',help='The sentence to decrypt from base64')
    parser.add_argument('--toBase64',help='The sentence to encrypt in base64')

    #Args fir RSA
    parser.add_argument("--toRsa", help="The file that you want to encrypt in Rsa with a public key or private key already created or create et pair of keys")
    parser.add_argument("-n", help="Specify the modulus.")
    parser.add_argument("-p", help="Specify the first prime number.")
    parser.add_argument("-q", help="Specify the second prime number.")
    parser.add_argument("-e", help="Specify the public exponent.")
    parser.add_argument("--privateKey", help="The private key in a file")
    parser.add_argument("--publicKey", help="The public key in a file")
    parser.add_argument("--RsaInFile", help="The flag encrypted in a file")
    parser.add_argument("--dumpKey", help="Dump the key, private or public")
    parser.add_argument("--genKeys", help="Generates a pair of keys")


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

    if args["base64"] != None:
        unBase64(args["base64"])

    if args["toBase64"] != None:
        codeInBase64(args["toBase64"])

    if args["toRsa"] != None:
        encryptInRsa(args["toRsa"],args["publicKey"],args["privateKey"])
    

    flag = args["RsaInFile"]
    privateK = args["privateKey"]
    publicK = args["publicKey"]
    if flag is not None:
        if privateK is not None:
            decryptRsa(flag,privateK)
        if publicK is not None:
            RsaDecryptWithPubKey(flag,publicK)
        else :
            print("You have to specify a privateKey")

    if args["dumpKey"] is not None:
        dumpKey(args["dumpKey"])
    
    if args["genKeys"] is not None :
        generateKeys()
    
    #If there is no argument specified : launch the help
    boolean = False
    for i in args:
        if args[i] is not None:
            boolean = True

    if boolean == False:
        os.system('/usr/bin/python DecrypTool.py -help')

    print("\n\tSee you later ! Keep doing some cryptography and hacking stuff\n\n")

#########################################################################################
#                               TransBase                                               #
#########################################################################################
def toBinary(value,fromBase):
    fromBase = fromBase.lower()
    if(fromBase == "decimal"):
        try:
            value = int(value)
            print(bin(value))
        except :
            print("It wasn't in decimal, try with another base")

    if(fromBase == "hexadecimal" or "hex"):
        try:
            valueHex = int(value, 16)
            hexaToBin = bin(valueHex)
            print(hexaToBin)
        except :
            print("It wasn't in hexadecimal, try with another base")

    if(fromBase == "octal"):
        try:
            valueOct = int(value,8)
            print(bin(valueOct))
        except :
            print("It wasn't in octal, try with another base")

def toDecimal(value,fromBase):
    fromBase = fromBase.lower()
    if(fromBase == "binary"):
        try:
            print(int(value,2))
        except :
            print("It wasn't in binary, try with another base")

    if(fromBase == "hexadecimal" or "hex"):
        try:
            valueHex = int(value, 16)
            print(valueHex)
        except :
            print("It wasn't in hexadecimal, try with another base")

    if(fromBase == "octal"):
        try:
            valueOct = int(value,8)
            print(valueOct)
        except :
            print("It wasn't in octal, try with another base")
    
def toHex(value,fromBase):
    fromBase = fromBase.lower()
    if(fromBase == "binary"):
        try:
            print(hex(int(value,2)))
        except :
            print("It wasn't in binary, try with another base")

    if(fromBase == "decimal"):
        try:
            value = int(value)
            print(hex(value))
        except :
            print("It wasn't in decimal, try with another base")

    if(fromBase == "octal"):
        try:
            valueOct = int(value,8)
            print(hex(valueOct))
        except :
            print("It wasn't in octal, try with another base")

def toOctal(value,fromBase):
    fromBase = fromBase.lower()
    if(fromBase == "binary"):
        try:
            o = int(value,2)
            print(oct(o))
        except :
            print("It wasn't in binary, try with another base")

    if(fromBase == "decimal"):
        try:
            value = int(value)
            print(oct(value))
        except :
            print("It wasn't in hexadecimal, try with another base")

    if(fromBase == "hexadecimal" or "hex"):
        try:
            o = int(value,16)
            print(oct(o))
        except :
            print("It wasn't in octal, try with another base")

############################################################################################
#                               Cesar's code                                               #
############################################################################################
def cesar(cesar) :

    print("The 26 possibilities :")
    liste_lettre=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    maj = ["A","B","C","D","E","F","G","H","i","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    phrase=cesar
    print(phrase)

    phrase_decodee=[]
    phrase=phrase.split()
    for pas in range (26) :
        for mot in phrase:
            liste_mot=[]
            for lettre in mot:
                if lettre in liste_lettre:
                    i=liste_lettre.index(lettre)
                    if i+pas>25:
                        i-=26
                    liste_mot.append(liste_lettre[i+pas])
                elif lettre in maj:
                    i=maj.index(lettre)
                    if i+pas>25:
                        i-=26
                    liste_mot.append(maj[i+pas])
                else :
                    liste_mot.append(lettre)
            phrase_decodee.append("".join(liste_mot))
        print(pas,"\t|"," ".join(phrase_decodee),"|")
        phrase_decodee = []
    

def unBase64(cipher):
    print(base64.b64decode(cipher[0]+"======"))

def codeInBase64(data):
    message = data[0]
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    print(base64_bytes)

###########################################################################
#                       RSA                                               # 
# Todo :                                                                  # 
# OpenSSL break certifs                                                   #
# decrypt with the public                                                 #
###########################################################################

def decryptRsa(flag, privkey):
    os.system('openssl rsautl -decrypt -inkey '+ privkey +' -in '+ flag)

def dumpKey(key):
    key_data = open(key, "rb").read()
    key = RSA.importKey(key_data)
    print("n: " + str(key.n))
    print("e: " + str(key.e))
    if key.has_private():
        print("d: " + str(key.d))
        print("p: " + str(key.p))
        print("q: " + str(key.q))


def RsaDecryptWithPubKey(file,publikey):
    os.system('openssl rsa -pubin -inform PEM -text -noout < '+publikey +' > resultDumpPubKey')

    key_data = open(publikey, "rb").read()
    key = RSA.importKey(key_data)
    n = str(key.n)
    e = str(key.e) 
    if key.has_private():
        d = str(key.d)
        p = str(key.p)
        q = str(key.q)

def generateKeys():
    os.system('openssl genrsa -out privateKey.pem')
    os.system('openssl rsa -in privateKey.pem -pubout -out publicKey.pem')
    print("Don't let anyone see your private key !")

def encryptInRsa(file,publicKey,privateKey):
    if publicKey != None:
        os.system('openssl rsautl -encrypt -in '+file+' -inkey '+publicKey+' -pubin -out ' + file+'.enc')
        print("You have encrypted your file with your public key")

    if privateKey != None:
        os.system('openssl rsautl -encrypt -in '+file+' -inkey '+privateKey+' -out ' + file+'.enc')
        print("You have encrypted your file with your private key")
    else :
        generateKeys()
        os.system('openssl rsautl -encrypt -in '+file+' -inkey publicKey.pem -pubin -out ' + file+'.enc')
        print("Now you have 3 files, the public key, the private one and your file encrypted")




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

