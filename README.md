# DecrypTool
### A tool which decrypt everything

# Table of content
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Code Exemples](#code-examples)
* [Upcoming](#upcoming)

# General info
It's a project built buy a 1st year student in IT.<br>
This programm has been made to make the cryptography easier for beginers. It as one objective :
**Make your ctf faster**<br>
I will regulary add new scripts and types of encryption / decryption.
Actually, DecrypTool has :
* Cesear bruteforce
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

# Technologies
I used python to make this tool, you will need the following extensions :
* os
* base64
* argparse

# Setup
## To run this script :
`git clone https://github.com/Amanatao/DecrypTool`|<br>
`pip3 install -r "requierment.txt"`<br>
`python3 DecrypTool.py`

# Code Examples
### The cesar mode :<br>
`python3 ./DecrypTool.py -c "Your sentence"`

### The base transposition mode : <br>
`python3 ./DecrypTool.py -toBinary "Your value" --from "The base that the value come from"`

### The RSA mode:<br>
#### To encrypt :<bR>
`python3 ./DecrypTool.py --toRSA "Your message" -e "The exponent" -n "The modulus"`

####  To decrypt if you have the cipher and the private key :<br>
`python3 ./DecrypTool.py --RsaInFile "Your file" --privateKey "Your private key"`

# Upcoming
* AES encryption / decryption.
* RSA encryption with private key and cracking with public key.
* Test all the possiblities if a base for transposition isn't specified