import argparse
import base64

def main() :


    parser = argparse.ArgumentParser(description=("Decrypt Everything !"))

    parser.add_argument('-c','--cesar',nargs= 1 , help='The sentence to decipher', required=False)

    parser.add_argument('-t', '--transBase', nargs=1, help='The "move to another base" mode ', required=False)

    parser.add_argument('-x','--xor', nargs=1, help='The unXOR mode', required=False)

    parser.add_argument('--base64',nargs=1,help='The sentence to decrypt from base64', required=False)

    parser.add_argument('--toBase64',nargs=1,help='The sentence to encrypt in base64', required=False)

    parser.add_argument("--rsa", help="Activates the RSA mode")

    parser.add_argument("-n", help="Specify the modulus. format : int or 0xhex")

    parser.add_argument("-p", help="Specify the first prime number. format : int or 0xhex")

    parser.add_argument("-q", help="Specify the second prime number. format : int or 0xhex")

    parser.add_argument("-e", help="Specify the public exponent. format : int or 0xhex")

    args = parser.parse_args()
    args = vars(args)

    toCesar = args["cesar"]
    toTransBase = args["transBase"]
    toXor = args["xor"]
    fromBase64 = args["base64"]
    toBase64 = args["toBase64"]

    rsa = args["rsa"]

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

    if rsa != None:
        p = args["p"]
        q = args["q"]
        n = args["n"]
        e = args["e"]

        if e is not None :
            if p is not None and q is not None:
                toRSA(rsa,e,p*q)
            elif n is not None :
                toRSA(rsa,e,n)
            else:
                print("You have to enter a modulus or a couple of prim numbers")
        else:
            print("You have to enter an exponent to make the RSA encryption")
       
        

def transBase(transBase) :

    if transBase != None:
        s = transBase[0]
    else : s =0 
    print('Le message a convertir : ', s)
    print('Le 0 en resultat signifie soit une valeur impossible, soit la valeur 0','\n')

    #Essaye de convertir en entier
    try :
        intS = int(s,10)
    except : 
        intS = 0

    print('intS = ' ,intS)

    #Essaye de convertir en octal
    try :
        octToDecimal = int(s,8)
        octS = oct(octToDecimal)
    except :
        octS = oct(0)
    print('octS = ',octS)

    #Essaye de convertir en biniare
    try : 
        binToIntS = int(s,2)
        binS = bin(binToIntS)
    except :
        binS = bin(0)
    print('binS = ',binS)

    #Essaye de convertir en hexa
    try : 
        hexToIntS = int(s,16)
        hexS = hex(hexToIntS)
    except :
        hexS = hex(0)
    print('hexS = ', hexS)


    #Si le message de base est en binaire 
    print('[~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~]','\n')
    print('Si c\'etait du binaire : ', '\n')

    print('En binaire : ','\t', binS, '\n')
    binToDecimal = int(binS,2)

    binToOctal = oct(binToDecimal)
    print('En octal : ','\t', binToOctal, '\n')

    binToDecimal = int(binS,2)
    print('En decimal : ' ,'\t', binToDecimal ,'\n')

    print('En hexa : ','\t', hex(binToDecimal),'\n')

    #Si le message de base etait en decimal
    print('[~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~]', '\n')
    print('Si le message etait en decimal')

    decimalToBin = bin(intS)
    print('En binaire : ','\t',decimalToBin,'\n')

    print('En octal : ','\t', oct(intS),'\n')

    print('En decimal : ','\t', intS,'\n')

    print('En hexa : ','\t', hex(intS))

    print('[~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~]', '\n')
    print('Si le message etait en hexadecimal')

    hexaToDecimal = int(hexS, 16)

    hexaToBin = int(hexS.lower(), 16)
    hexaToBin = bin(hexaToBin)
    print('En binaire : ','\t', hexaToBin, '\n')

    hexaToOct = oct(hexaToDecimal)
    print('En octal : ','\t', hexaToOct,'\n')

    print('En decimal : ','\t', hexaToDecimal,'\n')

    print('En hexa : ','\t', hexS, '\n')

    print('[~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~]', '\n')
    print('Si le message etait en octal','\n')

    octalToInt = int(octS,8)

    octalToBin = bin(octalToInt)
    print('En binaire : ','\t',octalToBin,'\n')

    print('En octal : ','\t',octS,'\n')

    print('En decimal : ','\t', octalToInt)

    octalToHex = hex(octalToInt)
    print('En hexa : ','\t', octalToHex, '\n')
    print('[~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~]')


#Chiffrement par decalage 
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

def unBase64(cypher):
    print(base64.b64decode(cypher[0]+"======"))

def codeInBase64(data):
    message = data[0]
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    print(base64_bytes)



def toRSA(message,theModulus,theE):
    toCypher = message[0]
    modulus = theModulus[0]
    e = theE[0]

    cypher = pow(toCypher,e,modulus)
    print(cypher)






def banner() :
    print("""
  ____                           _____           _ 
 |  _ \  ___  ___ _ __ _   _ _ _|_   _|__   ___ | |
 | | | |/ _ \/ __| '__| | | | '_ \| |/ _ \ / _ \| |
 | |_| |  __/ (__| |  | |_| | |_) | | (_) | (_) | |
 |____/ \___|\___|_|   \__, | .__/|_|\___/ \___/|_|
                       |___/|_|                    
    """)
    print('\n\t\t',"Welcome to DecrypTool\n\n\n")


if __name__ == '__main__' :
    main()

"""
To do :
ROT 13
XOR
ASCII
"""