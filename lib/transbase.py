import base64
def toBinary(value,fromBase):
    fromBase = fromBase.lower()
    if(fromBase == "decimal"):
        try:
            value = int(value)
            print(bin(value))
        except :
            print("It wasn't in decimal, try with another base")

    if(fromBase == "hexadecimal" or "hex"):
        try:
            valueHex = int(value, 16)
            hexaToBin = bin(valueHex)
            return hexaToBin
        except :
            print("It wasn't in hexadecimal, try with another base")

    if(fromBase == "octal"):
        try:
            valueOct = int(value,8)
            return bin(valueOct)
        except :
            print("It wasn't in octal, try with another base")

def toDecimal(value,fromBase):
    fromBase = fromBase.lower()
    if(fromBase == "binary"):
        try:
            print(int(value,2))
        except :
            print("It wasn't in binary, try with another base")

    if(fromBase == "hexadecimal" or "hex"):
        try:
            valueHex = int(value, 16)
            print(valueHex)
        except :
            print("It wasn't in hexadecimal, try with another base")

    if(fromBase == "octal"):
        try:
            valueOct = int(value,8)
            print(valueOct)
        except :
            print("It wasn't in octal, try with another base")
    
def toHex(value,fromBase):
    fromBase = fromBase.lower()
    if(fromBase == "binary"):
        try:
            print(hex(int(value,2)))
        except :
            print("It wasn't in binary, try with another base")

    if(fromBase == "decimal"):
        try:
            value = int(value)
            print(hex(value))
        except :
            print("It wasn't in decimal, try with another base")

    if(fromBase == "octal"):
        try:
            valueOct = int(value,8)
            print(hex(valueOct))
        except :
            print("It wasn't in octal, try with another base")

def toOctal(value,fromBase):
    fromBase = fromBase.lower()
    if(fromBase == "binary"):
        try:
            o = int(value,2)
            print(oct(o))
        except :
            print("It wasn't in binary, try with another base")

    if(fromBase == "decimal"):
        try:
            value = int(value)
            print(oct(value))
        except :
            print("It wasn't in hexadecimal, try with another base")

    if(fromBase == "hexadecimal" or "hex"):
        try:
            o = int(value,16)
            print(oct(o))
        except :
            print("It wasn't in octal, try with another base")

def fromBase64(cipher):
    print(base64.b64decode(cipher[0]+"======"))

def toBase64(data):
    message = data[0]
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    print(base64_bytes)