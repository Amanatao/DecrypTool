# DecrypTool
### A tool which decrypt everything

# __Table of content__
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Code Exemples](#code-examples)
* [Upcoming](#upcoming)

# __General info__
It is a project built by a 1st year student in IT.<br>
This program has been created to make cryptography easier for beginners. It has one objective :
**Make your ctf faster**<br>
I will regularly add new scripts and types of encryption / decryption.
To date, DecrypTool has :
* Cesar bruteforce
* Base transposition : 
    * Binary
    * Octal
    * Decimal
    * Hexadecimal
    * Base64
* RSA 
    * Encryption
    * Decryption with the private key
    * Dumping the private key to obtain the exponent, modulus, the 2 primes

# __Technologies__
I used python to make this tool, you will need the following extensions :
* os
* base64
* argparse
* openssl

# __Setup__
## To run this script :
```
git clone https://github.com/Amanatao/DecrypTool<br>
pip3 install -r "requirement.txt"<br>
python3 DecrypTool.py
```

# __Code Examples__
## __The cesar mode :__<br>
`python3 ./DecrypTool.py -c "Your sentence"`

## __The base transposition mode :__ <br>
`python3 ./DecrypTool.py -toBinary "Your value" --from "The base that the value come from"`

## __The RSA mode:__<br>
### **To encrypt :**<br>
Without keys :<br>
`python3 ./DecrypTool.py --toRSA "Your file"`<br>
With a public key:<br>
`python3 ./DecrypTool.py --toRsa "Your file" --publicKey`<br>
With a private key:<br>
`python3 ./DecrypTool.py --toRsa "Your file" --privateKey`<br>

###  **To decrypt if you have the cipher and the private key :**<br>
`python3 ./DecrypTool.py --RsaInFile "Your file" --privateKey "Your private key"`

### **To generate a pair of keys**
`python3 ./DecrypTool.py --genKeys`
# __Upcoming__
* AES encryption / decryption.
* RSA cracking with public key.
* Test all the possiblities if a base for transposition isn't specified
* A website ! For the windows user who want to use my code !
