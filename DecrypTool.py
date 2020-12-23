import binascii
<<<<<<< HEAD
=======

>>>>>>> 037f54f8b02e15671e107519d9bf364b30869dfe
s = input('Veuillez renseigner un message crypte : ')
print('Le message a decrypter : ', s)

# ~~ Convertit le string en int
intS= int(s)


#Les bases supportees sont : 2 (binaire) / 8 (octal) / 10 (decimal) / 16 (hexa)

# ~~ Conversion en binaire
print('[/] Conversion en Binaire \n' )
<<<<<<< HEAD
=======
def bin(n):
    if n == 0: return '0'
    res = ''
    while n != 0: n, res = n >> 1, repr(n & 1) + res
    return res

>>>>>>> 037f54f8b02e15671e107519d9bf364b30869dfe
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

<<<<<<< HEAD

#Chiffrement par decalage 

liste_lettre=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

phrase=(input("Votre phrase : ")).lower()

phrase_codee=[]
phrase=phrase.split()
for pas in range (25) :
    for mot in phrase:
        liste_mot=[]
        for lettre in mot:
            i=liste_lettre.index(lettre)
            if i+pas>25:
                i-=26
            liste_mot.append(liste_lettre[i+pas])
        phrase_codee.append("".join(liste_mot))
    print(pas," ".join(phrase_codee))



=======
>>>>>>> 037f54f8b02e15671e107519d9bf364b30869dfe

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
<<<<<<< HEAD
- C'est de l'octal -> On le convertit en binaire et ensuite binascii
- C'est du decimal -> hex()
- C'est de l'hexa -> On retourne la même chose

Decallage cesar
On defini un tableau avec pour chaque indice une lettre de l'alphabet
Ensuite on divise la chaine de caractères en un tableau avec une case pour chaque lettre.
et ensuite on echange.
=======
>>>>>>> 037f54f8b02e15671e107519d9bf364b30869dfe
"""


    

    

