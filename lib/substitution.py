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