import argparse
import base64
import os

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


    #Args for xor
    parser.add_argument('-x','--xor', help='The unXOR mode')

    #Args for Base64
    parser.add_argument('--base64',help='The sentence to decrypt from base64')
    parser.add_argument('--toBase64',help='The sentence to encrypt in base64')

    #Args fir RSA
    parser.add_argument("--toRsa", help="Activates the RSA mode")
    parser.add_argument("-n", help="Specify the modulus. format : int or 0xhex")
    parser.add_argument("-p", help="Specify the first prime number. format : int or 0xhex")
    parser.add_argument("-q", help="Specify the second prime number. format : int or 0xhex")
    parser.add_argument("-e", help="Specify the public exponent. format : int or 0xhex")
    parser.add_argument("--privateKey", help="The private key in a file")
    parser.add_argument("--RsaInFile", help="The flag encrypted in a file")
    parser.add_argument("--dump", help="Dump the private key")


    args = parser.parse_args()
    args = vars(args)

    banner()
    if args["toDecimal"] is not None and args["from"] is not None:
        toDecimal(args["toDecimal"],args["from"])

    if args["toHex"] is not None and args["from"] is not None:
        toDecimal(args["toHex"],args["from"])

    if args["toOctal"] is not None and args["from"] is not None:
        toDecimal(args["toOctal"],args["from"])
    
    if args["toBinary"] is not None and args["from"] is not None:
        toDecimal(args["toBinary"],args["from"])

    if args["cesar"] !=  None:
        cesar(args["cesar"])
        
    if args["xor"] != None :
        xor(args["xor"])

    if args["base64"] != None:
        unBase64(args["base64"])

    if args["toBase64"] != None:
        codeInBase64(args["toBase64"])

    if args["toRsa"] != None:
        p = args["p"]
        q = args["q"]
        n = args["n"]
        e = args["e"]
        

        if e is not None :
            if p is not None and q is not None:
                toRSA(args["toRsa"],e,p*q)
            elif n is not None :
                toRSA(args["toRsa"],e,n)
            else:
                print("You have to enter a modulus or a couple of prim numbers")
        else:
            print("You have to enter an exponent to make the RSA encryption")

    flag = args["RsaInFile"]
    privateK = args["privateKey"]   
    if flag is not None:
        if privateK is not None:
            opensslRsa(flag,privateK)
        else :
            print("You have to specify a privateKey")

    dump = args["dump"]
    if dump is not None:
        dumpPrivateKey(dump)
    
    #If there is no argument specified : launch the help
    boolean = False
    for i in args:
        if args[i] is not None:
            boolean = True

    if boolean == False:
        os.system('/usr/bin/python DecrypTool.py -help')


#########################################################################################
#                           TransBase
#Todo:
#Make it "smoother", it's actually ugly
#########################################################################################
def toBinary(value,fromBase):
    fromBase = fromBase.lower()
    if(fromBase == "decimal"):
        try:
            print(bin(value))
        except :
            print("It wasn't in decimal, try with another base")

    if(fromBase == "hexadecimal"):
        try:
            valueHex = int(value, 16)
            hexaToBin = bin(hexaToBin)
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

    if(fromBase == "hexadecimal"):
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
            print(oct(value))
        except :
            print("It wasn't in hexadecimal, try with another base")

    if(fromBase == "hexadecimal"):
        try:
            o = int(value,16)
            print(oct(o))
        except :
            print("It wasn't in octal, try with another base")

############################################################################################
#                   Cesar's code
#Todo:
#Keep the caps in the final message, actually only in lower case
############################################################################################
def cesar(cesar) :

    print("The 26 possibilities :")
    liste_lettre=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    phrase=cesar[0]
    print(phrase)

    phrase_decodee=[]
    phrase = phrase.lower()
    phrase=phrase.split()
    for pas in range (26) :
        for mot in phrase:
            liste_mot=[]
            for lettre in mot:
                i=liste_lettre.index(lettre)
                if i+pas>25:
                    i-=26
                liste_mot.append(liste_lettre[i+pas])
            phrase_decodee.append("".join(liste_mot))
        print(pas,"\t|"," ".join(phrase_decodee),"|")
        phrase_decodee = []

def xor(xor) :
    print('*unXOR code*')

def unBase64(cipher):
    print(base64.b64decode(cipher[0]+"======"))

def codeInBase64(data):
    message = data[0]
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    print(base64_bytes)

###########################################################################
#                       RSA 
# Todo : 
# OpenSSL break certifs
# Crypt with the private key and decrypt with the public
###########################################################################


def toRSA(message,theModulus,theE):
    toCipher = message[0]
    modulus = theModulus[0]
    e = theE[0]

    cipher = pow(toCipher,e,modulus)
    print(cipher)

def opensslRsa(flag, privkey):
    os.system('openssl rsautl -decrypt -inkey '+ privkey +' -in '+ flag + ' -out result')

def dumpPrivateKey(privkey):
    os.system('openssl rsa -in '+privkey+' -text -noout')


            

            





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

