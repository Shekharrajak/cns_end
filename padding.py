# After padding (CMS): 68656c6c6f3132330808080808080808
# Cipher (ECB): aa9accd8acdb337fe6dba0bbfe426070
#   decrypt: hello123

# After padding (Bit): 68656c6c6f3132338000000000000000
# Cipher (ECB): 0f6c3077e6838ab6b5a1dc1ee6afd8e3
#   decrypt: hello123

# After padding (ZeroLen): 68656c6c6f3132330000000000000007
# Cipher (ECB): 38350f339c87ecf98a5035eddaf28ea7
#   decrypt: hello123�

# After padding (Null): 68656c6c6f3132330000000000000000
# Cipher (ECB): 38f1e8924bd807d926e9df17ba4db72e
#   decrypt: hello123

# After padding (Space): 68656c6c6f3132330000000000000000
# Cipher (ECB): 38f1e8924bd807d926e9df17ba4db72e
#   decrypt:

# After padding (Random): 68656c6c6f313233e5fa500d0def3f07
# Cipher (ECB): 128c2ed64c7717c4adeb1833059767e2
#   decrypt: hello123å


from Crypto.Cipher import AES
import hashlib
import sys
import binascii
import Padding

val='hello'
password='hello'

plaintext=val

def encrypt(plaintext,key, mode):
    encobj = AES.new(key,mode)
    return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
    encobj = AES.new(key,mode)
    return(encobj.decrypt(ciphertext))

key = hashlib.sha256(password).digest()


plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode='CMS')
print "After padding (CMS): "+binascii.hexlify(bytearray(plaintext))

ciphertext = encrypt(plaintext,key,AES.MODE_ECB)
print "Cipher (ECB): "+binascii.hexlify(bytearray(ciphertext))

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
plaintext = Padding.removePadding(plaintext,mode='CMS')
print "  decrypt: "+plaintext


plaintext=val


plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode='ZeroLen')
print "\nAfter padding (Bit): "+binascii.hexlify(bytearray(plaintext))

ciphertext = encrypt(plaintext,key,AES.MODE_ECB)
print "Cipher (ECB): "+binascii.hexlify(bytearray(ciphertext))

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
plaintext = Padding.removePadding(plaintext,blocksize=Padding.AES_blocksize,mode='ZeroLen')
print "  decrypt: "+plaintext


plaintext=val

plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode='Space')
print "\nAfter padding (Null): "+binascii.hexlify(bytearray(plaintext))

ciphertext = encrypt(plaintext,key,AES.MODE_ECB)
print "Cipher (ECB): "+binascii.hexlify(bytearray(ciphertext))

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
plaintext = Padding.removePadding(plaintext,blocksize=Padding.AES_blocksize,mode='Space')
print "  decrypt: "+plaintext


plaintext=val

plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode='Random')
print "\nAfter padding (Random): "+binascii.hexlify(bytearray(plaintext))

ciphertext = encrypt(plaintext,key,AES.MODE_ECB)
print "Cipher (ECB): "+binascii.hexlify(bytearray(ciphertext))

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
plaintext = Padding.removePadding(plaintext,mode='Random')
print "  decrypt: "+plaintext
