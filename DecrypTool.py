import argparse
import base64
import os

def main() :


    parser = argparse.ArgumentParser(description=("Decrypt Everything !"))

    #Args for cesar
    parser.add_argument('-c','--cesar',nargs= 1 , help='The sentence to decipher', required=False)

    #Args for Transbase
    parser.add_argument('-t', '--transBase', nargs=1, help='The "move to another base" mode ', required=False)

    #Args for xor
    parser.add_argument('-x','--xor', nargs=1, help='The unXOR mode', required=False)

    #Args for Base64
    parser.add_argument('--base64',nargs=1,help='The sentence to decrypt from base64', required=False)
    parser.add_argument('--toBase64',nargs=1,help='The sentence to encrypt in base64', required=False)

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

    toCesar = args["cesar"]
    toTransBase = args["transBase"]
    toXor = args["xor"]
    fromBase64 = args["base64"]
    toBase64 = args["toBase64"]

    toRsa = args["toRsa"]

    banner()
    if toCesar !=  None:
        cesar(toCesar)
    
    if toTransBase != None :
        transBase(toTransBase)
    
    if toXor != None :
        xor(toXor)

    if fromBase64 != None:
        unBase64(fromBase64)

    if toBase64 != None:
        codeInBase64(toBase64)

    if toRsa != None:
        p = args["p"]
        q = args["q"]
        n = args["n"]
        e = args["e"]
        

        if e is not None :
            if p is not None and q is not None:
                toRSA(toRsa,e,p*q)
            elif n is not None :
                toRSA(toRsa,e,n)
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
def transBase(transBase) :

    if transBase != None:
        s = transBase[0]
    else : s =0 
    print('Le message a convertir : ', s)
    print('Le 0 en resultat signifie soit une valeur impossible, soit la valeur 0','\n')

    #Try to convert in decimal
    try :
        intS = int(s,10)
    except : 
        intS = 0

    #Try to convert in octal
    try :
        octToDecimal = int(s,8)
        octS = oct(octToDecimal)
    except :
        octS = oct(0)

    #Try to convert in binary
    try : 
        binToIntS = int(s,2)
        binS = bin(binToIntS)
    except :
        binS = bin(0)

    #Try to convert in hex
    try : 
        hexToIntS = int(s,16)
        hexS = hex(hexToIntS)
    except :
        hexS = hex(0)


    #If the message is in binary
    print('[~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~]','\n')
    print('If the message is in binary : ', '\n')

    print('In binary : ','\t', binS, '\n')
    binToDecimal = int(binS,2)

    binToOctal = oct(binToDecimal)
    print('In octal : ','\t', binToOctal, '\n')

    binToDecimal = int(binS,2)
    print('In decimal : ' ,'\t', binToDecimal ,'\n')

    print('In hexa : ','\t', hex(binToDecimal),'\n')

    #If the message is in decimal
    print('[~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~]', '\n')
    print('If the message is in decimal')

    decimalToBin = bin(intS)
    print('In binary : ','\t',decimalToBin,'\n')

    print('In octal : ','\t', oct(intS),'\n')

    print('In decimal : ','\t', intS,'\n')

    print('In hexa : ','\t', hex(intS))

    print('[~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~]', '\n')
    print('If the message is in hexadecimal')

    hexaToDecimal = int(hexS, 16)

    hexaToBin = int(hexS.lower(), 16)
    hexaToBin = bin(hexaToBin)
    print('In binary : ','\t', hexaToBin, '\n')

    hexaToOct = oct(hexaToDecimal)
    print('In octal : ','\t', hexaToOct,'\n')

    print('In decimal : ','\t', hexaToDecimal,'\n')

    print('In hexa : ','\t', hexS, '\n')

    print('[~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~]', '\n')
    print('Si le message etait en octal','\n')

    octalToInt = int(octS,8)

    octalToBin = bin(octalToInt)
    print('In binary : ','\t',octalToBin,'\n')

    print('In octal : ','\t',octS,'\n')

    print('In decimal : ','\t', octalToInt)

    octalToHex = hex(octalToInt)
    print('In hexa : ','\t', octalToHex, '\n')
    print('[~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~]')


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

