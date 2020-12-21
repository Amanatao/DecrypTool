import binascii

s = input('Veuillez renseigner un message crypte : ')
print('Le message a decrypter : ', s)

# ~~ Convertit le string en int
intS= int(s)


#Les bases supportees sont : 2 (binaire) / 8 (octal) / 10 (decimal) / 16 (hexa)

# ~~ Conversion en binaire
print('[/] Conversion en Binaire \n' )
def bin(n):
    if n == 0: return '0'
    res = ''
    while n != 0: n, res = n >> 1, repr(n & 1) + res
    return res

binaire = bin(intS)
print('En binaire : ', binaire)

# ~~ Conversion en octal
print('[/] Conversion en Octal \n')
octal = oct(intS)
print('En octal : ' , octal)

# ~~ Conversion en decimal
print('[/] Conversion en Decimal \n')
decimalH = int(s,16)
print('Si le message etait en hexa : ' , decimalH ,'\n')

decimalBin = int(s,2)
print('Si le message etait en binaire : ' , decimalBin ,'\n')

decimalOct = int(s,8)
print('Si le message etait en octal : ', decimalOct ,'\n')

# ~~ Conversion en hexa
print('[/] Conversion en Hexa \n')
hexa = hex(s)
print('En hexa : ', hexa, '\n')


"""
Toutes les possibilités : 

Transformer en Binaire :
- C'est déjà du binaire -> On retourne la même chose
- C'est du decimal -> bin()
- C'est de l'octal -> Split chaque nombre et prendre le code binaire de chacun
- C'est de l'hexa -> binascii

Transformer en decimal :
- C'est du binaire -> int(x,2)
- C'est de l'octal -> int(x,8)
- C'est déjà du decimal -> (x,10)
- C'est de l'hexa -> int(x,16)

Transformer en hexa : 
- C'est du binaire -> binascii
"""


    

    

