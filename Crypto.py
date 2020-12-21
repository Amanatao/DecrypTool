s = input('Veuillez renseigner un message crypte : ')
print ('Le message a decrypter : ', s)

#Les bases supportees sont : 2 (binaire) / 8 (octal) / 10 (decimal) / 16 (hexa)

def toBinary (s) :
    print ('Si c\' etait du decimal')

    plusG = false
    i = 0
    while plusG==false :
        if 2^i < s :
            i = i+1
        else :
            i = i -1
            plusG = true
    

