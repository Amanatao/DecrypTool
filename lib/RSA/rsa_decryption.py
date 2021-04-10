import os
from Crypto.PublicKey import RSA

def dumpKey(key):
    key_data = open(key, "rb").read()
    key = RSA.importKey(key_data)
    print("n: " + str(key.n))
    print("e: " + str(key.e))
    if key.has_private():
        print("d: " + str(key.d))
        print("p: " + str(key.p))
        print("q: " + str(key.q))


def RsaDecryptWithPrivKey(flag, privkey):
    os.system('openssl rsautl -decrypt -inkey '+ privkey +' -in '+ flag)

def RsaDecryptWithPubKey(file,publikey):
    os.system('openssl rsa -pubin -inform PEM -text -noout < '+publikey +' > resultDumpPubKey')

    key_data = open(publikey, "rb").read()
    key = RSA.importKey(key_data)
    n = str(key.n)
    e = str(key.e)