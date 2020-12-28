import argparse

def main() :
    #Variables
    toCesar = ""
    toTransBase = ""
    toXor = ""
    toRot13 = ""
    
    parser = argparse.ArgumentParser(description=("Decrypt Everything"))

    parser.add_argument('-c','--cesar',nargs= 1 , help='The sentence to decipher', required=False)

    parser.add_argument('-t', '--transBase', nargs=1, help='What do you want to move to another base', required=False)

    parser.add_argument('-x','--xor', nargs=1, help='What do you want to "unXOR"', required=False)

    parser.add_argument('--rot13', nargs=1, help='The thing to be transforme by ROT13', required=False)

    args = parser.parse_args()
    args = vars(args)

    toCesar = args[cesar]
    toTransBase = args[transBase]
    toXor = args[xor]
    toRot13 = args[rot13]

    banner()
    
    if toCesar != "" :
        cesar(toCesar)
    
    if toTransBase != "" :
        transBase(toTransBase)
    
    if toXor != "" :
        xor(toXor)
    
    if toRot13 != "" :
        rot13(toRot13)

def transBase(transBase) :
    s = transBase
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

    liste_lettre=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    phrase=cesar

    phrase_codee=[]
    phrase=phrase.split()
    for pas in range (26) :
        for mot in phrase:
            liste_mot=[]
            for lettre in mot:
                i=liste_lettre.index(lettre)
                if i+pas>25:
                    i-=26
                liste_mot.append(liste_lettre[i+pas])
            phrase_codee.append("".join(liste_mot))
        
        print(pas," ".join(phrase_codee))
        phrase_codee = []


def xor(xor) :
    print('*xor code ')

def rot13(rot13) :
    print('*Rot13 code*')

def banner() :
    print("""
  ____                           _____           _ 
 |  _ \  ___  ___ _ __ _   _ _ _|_   _|__   ___ | |
 | | | |/ _ \/ __| '__| | | | '_ \| |/ _ \ / _ \| |
 | |_| |  __/ (__| |  | |_| | |_) | | (_) | (_) | |
 |____/ \___|\___|_|   \__, | .__/|_|\___/ \___/|_|
                       |___/|_|                    
    """)
    print('\n',"Welcome at DecrypTool")
if __name__ == '__main__' :
    main()

"""
To do :
ROT 13
XOR
ASCII
"""
