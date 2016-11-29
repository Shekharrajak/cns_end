# If we use "hello", then we must pad to 5 bytes, this means there are 3 padding bytes (0x3) to give:

# After padding (CMS): 68656c6c6f030303
# Cipher (ECB): 8f770898ddb9fb38
#   decrypt: hello
# If we use "hello1", then we must pad to 6 bytes, this means there are 2 padding bytes (0x2) to give:

# After padding (CMS): 68656c6c6f310202
# Cipher (ECB): 602743be4d9c6f17
#   decrypt: hello1


from Crypto.Cipher import DES
import hashlib
import sys
import binascii
import Padding

val='hello'
password='hello'

plaintext=val


def encrypt(plaintext,key, mode):
    encobj = DES.new(key,mode)
    return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
    encobj = DES.new(key,mode)
    return(encobj.decrypt(ciphertext))


print "\nDES"
key = hashlib.sha256(password).digest()[:8]

plaintext = Padding.appendPadding(plaintext,blocksize=Padding.DES_blocksize,mode='CMS')
print "After padding (CMS): "+binascii.hexlify(bytearray(plaintext))

ciphertext = encrypt(plaintext,key,DES.MODE_ECB)
print "Cipher (ECB): "+binascii.hexlify(bytearray(ciphertext))

plaintext = decrypt(ciphertext,key,DES.MODE_ECB)
plaintext = Padding.removePadding(plaintext,mode='CMS')
print "  decrypt: "+plaintext
