# sample run with an IV of 3, and data of "hello" and a password of "napier123"

# IV: 0000000000000003
# Input data (CMS): 68656c6c6f0b0b0b0b0b0b0b0b0b0b0b
# Cipher (ECB): 0a7ec77951291795bac6690c9e7f4c0d
#   decrypt: hello
# Cipher (CBC): c91f59b001f502bec8c8359796d63d68
#   decrypt: hello
# Cipher (CFB): 5724326a85c1afba88dc936f590ac1ba
#   decrypt: hello
# Cipher (OFB): 5773f7c72bb54e13bf807c22c21cdb31
#   decrypt: hello


from Crypto.Cipher import AES
import hashlib
import sys
import binascii
import Padding

val='hello'
password='hello'
ival=10


plaintext=val

def encrypt(plaintext,key, mode):
    encobj = AES.new(key,mode)
    return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
    encobj = AES.new(key,mode)
    return(encobj.decrypt(ciphertext))

def encrypt2(plaintext,key, mode,iv):
    encobj = AES.new(key,mode,iv)
    return(encobj.encrypt(plaintext))

def decrypt2(ciphertext,key, mode,iv):
    encobj = AES.new(key,mode,iv)
    return(encobj.decrypt(ciphertext))


key = hashlib.sha256(password).digest()

iv= hex(ival)[2:8].zfill(16)



print "IV: "+iv


plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode=0)
print "Input data (CMS): "+binascii.hexlify(bytearray(plaintext))

ciphertext = encrypt(plaintext,key,AES.MODE_ECB)
print "Cipher (ECB): "+binascii.hexlify(bytearray(ciphertext))

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
plaintext = Padding.removePadding(plaintext,mode=0)
print "  decrypt: "+plaintext


plaintext=val
plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode=0)

ciphertext = encrypt2(plaintext,key,AES.MODE_CBC,iv)
print "Cipher (CBC): "+binascii.hexlify(bytearray(ciphertext))

plaintext = decrypt2(ciphertext,key,AES.MODE_CBC,iv)
plaintext = Padding.removePadding(plaintext,mode=0)
print "  decrypt: "+plaintext



plaintext=val
plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode=0)

ciphertext = encrypt2(plaintext,key,AES.MODE_CFB,iv)
print "Cipher (CFB): "+binascii.hexlify(bytearray(ciphertext))

plaintext = decrypt2(ciphertext,key,AES.MODE_CFB,iv)
plaintext = Padding.removePadding(plaintext,mode=0)
print "  decrypt: "+plaintext



plaintext=val
plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode=0)

ciphertext = encrypt2(plaintext,key,AES.MODE_OFB,iv)
print "Cipher (OFB): "+binascii.hexlify(bytearray(ciphertext))

plaintext = decrypt2(ciphertext,key,AES.MODE_OFB,iv)
plaintext = Padding.removePadding(plaintext,mode=0)
print "  decrypt: "+plaintext
