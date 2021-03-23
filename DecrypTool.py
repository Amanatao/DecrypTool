import argparse
import base64

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


    #Args for Vigenere
    parser.add_argument("--vigenereCode", help="The message to cipher in Vigenere")
    parser.add_argument("--vigenereDecode", help="The message to decrypt from Vigenere")
    parser.add_argument("--vigenereKey", help="The key if you have it")
    


    args = parser.parse_args()
    args = vars(args)

    toCesar = args["cesar"]
    toTransBase = args["transBase"]
    toXor = args["xor"]
    fromBase64 = args["base64"]
    toBase64 = args["toBase64"]

    toRsa = args["toRsa"]

    toVigenere = args["vigenereCode"]
    fromVigenere = args["vigenereDecode"]

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
       
    if toVigenere is not None:
        key = args["vigenereKey"]
        if key is not None:
            CodeVigenere(toVigenere,key)
        else :
            print("You have to enter en correct key")

    if fromVigenere is not None:
        key = args["vigenereKey"]
        if key is not None:
            DecodeVigenere(fromVigenere,key)
        else :
            DecodeVigenereWithoutKey(fromVigenere)
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


############################################################################################
#                   Cesar's code
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
###########################################################################


def toRSA(message,theModulus,theE):
    toCipher = message[0]
    modulus = theModulus[0]
    e = theE[0]

    cipher = pow(toCipher,e,modulus)
    print(cipher)


###########################################################################
#                   Vigenere
###########################################################################

def DecodeVigenereWithoutKey(message):
    lengthKey = DecodeVigenereLongueurCle(message)
    key = DecodeVigenereCle(message,lengthKey)
    print("The decrypted Vigenere message :",DecodeVigenere(message, key))

def CodeVigenere(message, cle):
    print("The original message : ",message,"\tThe given key : ",cle,"\tThe cipher : ", code_vigenere(message, cle))
    

def code_vigenere ( message, cle, decode = False) :
    message_code = ""
    for i,c in enumerate(message) :
        d = cle[ i % len(cle) ]
        d = ord(d) - 65
        if decode : d = 26 - d
        message_code += chr((ord(c)-65+d)%26+65)
    return message_code

def DecodeVigenere(message, cle):
    print(code_vigenere(message, cle, True)) 


def PGCD (m,n) :
    if m <= 0 or n <= 0 : raise Exception("impossible de calculer le PGCD")
    if m == 1 or n == 1 : return 1
    if m == n : return m
    if m < n : return PGCD (m, n-m)
    return PGCD (n, m-n)

def DecodeVigenereLongueurCle (message, mot = 3) :
    """
    cette fonction determine la longueur de la clé, elle
    repère les groupes de trois lettres qui se répète dans le message codé
    et suppose qu'il y a une très forte probabilité qu'un même groupe de trois
    lettres soit codé avec les mêmes trois lettres du message et les mêmes trois
    lettres de la clé

    message  : .....DES...........DES...........DES.........DES....DES
    cle      : ABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABCD
    code     : .....EGV.........................EGV.........EGV..........
    distance :      <----------24--------------><----8----->

    la longueur de la clé divise le PGCD de 24 et 8
    """
    al = "".join([ chr(97+i) for i in range(0,26) ]) # l'alphabet
    al = al.upper ()

    # parcours du message pour recenser toutes les positions
    dico = {}
    for i in range (0, len (message)-2) :
        t = message [i:i+mot]
        if t in dico : dico [t].append (i)
        else : dico [t] = [i]

    # on va garder toutes les distances entre
    # entre deux occurrences du meme mot de n lettres
    dis = []
    for d in dico :
        p = dico [d]
        if len (p) > 1 :
            for i in range (0, len (p)-1) :
                #print d, p [i+1] - p [i], " --- ", float (p [i+1] - p [i]) / 8
                dis.append ( p [i+1] - p [i] )

    # on extrait le PGCD
    if len (dis) == 0 :
        raise Exception("impossible de determiner la clé")

    if len (dis) == 1 : return dis [0]

    longueur = PGCD (dis [0], dis [1])
    for d in dis :
        longueur = PGCD (longueur, d)

    if longueur > 5 :
        # si la longueur est suffisante, le resultat a des chances d'etre bon
        return longueur
    else :
        # sinon, on relance l'algorithme avec des mots plus grand
        return DecodeVigenereLongueurCle (message, mot+1)


def DecodeVigenereCle (code, l) :
    """
    Détermine la cle du message code, connaissant sa longueur,
    on suppose que la lettre E est la lettre la plus fréquente

    @param      code        message codé
    @param      l           longueur probable de la clé
    @return                 message décodé
    """
    al  = "".join([ chr(97+i) for i in range(0,26) ])
    al  = al.upper ()
    cle = ""
    for i in range (0, l) :
        nombre = [ 0 for a in al]
        sous   = code [i:len (code):l]  # on extrait toutes les lettres
                                        # i, i+l, i+2l; i+3l, ...

        # on compte les lettres
        for k in sous : nombre [ al.find (k) ] += 1

        # on cherche le maximum
        p = 0
        for k in range (0, len (nombre)) :
            if nombre [k] > nombre [p] : p = k

        # on suppose que al [p] est la lettre E code,
        # il ne reste plus qu'a trouver la lettre de la cle
        # qui a permis de coder E en al [p]
        cle += al [ (p + 26 - al.find ("E")) % 26 ]

    return cle



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

