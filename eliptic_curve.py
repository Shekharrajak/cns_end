# ++++Keys++++
# Bob's private key: 02da0024026c6aeccf91e869dac11b5dc6b5fd9d2b532d12ba63926cf59a8d0c2b5d9100b69be9e7
# Bob's public key: 02da00240727903797335fd45d88ddb16253b8e17448f6fbf138c7dc37fa2869145e4eaaf02aae08002349ee164660dc9d55eb90e4d2d7e77b4176b16ff0e879a38520ec83b71c78c13456c0cf

# Alices's private key: 02da002329e3ca0ca45072e54c287a79a11fbe0e9571fd88c251ccbb8c5b474d6c016356886ba0
# Alices's public key: 02da002406f215ffee3b640145792655e53d00ca24cd013c5e135814c1c71859fdb687b5f605f985002403e555632044d13d57565bed9e91924cb2f711c4fdeef6ad8116abfb23722d71c6ef537e
# Now we can encrypted and decrypt, and also check the signature:

# ++++Encryption++++
# Cipher: b1d00002a091e2f88b7f90c1dd0271fa02da002405dbc5e79890c17f5f42401c0e1081d2ace03f80b9275759d4d0cd6535fa10b96357f058002403b0b71679f91f84e7c7de78a97886ccabd6326f1c7edfbcf5392e902d3aa7614d9f8e493d49f39ec95c0fdfe7bf9dc49de550e48fd323174952312be900ca697d5381f1288e8cf30841cf970adee6b1126a2e20
# Decrypt: Test123

# Bob verified: True
# Elliptic Curve can be used to generate a shared key:

# ++++ECDH++++
# Alice:6fd6156c4e5af0cd911eb89b4e8bfe9edee7adcc6f740b59a31cb2994b61abf4a32c3e2c0f8958841742770bba1123e620eea1dc702f96536c22cae5efb2910c

# Bob: 6fd6156c4e5af0cd911eb89b4e8bfe9edee7adcc6f740b59a31cb2994b61abf4a32c3e2c0f8958841742770bba1123e620eea1dc702f96536c22cae5efb2910c

import OpenSSL
import pyelliptic

secretkey="password"
test="Test123"

alice = pyelliptic.ECC()
bob = pyelliptic.ECC()

print "++++Keys++++"
print "Bob's private key: "+bob.get_privkey().encode('hex')
print "Bob's public key: "+bob.get_pubkey().encode('hex')

print
print "Alices's private key: "+alice.get_privkey().encode('hex')
print "Alices's public key: "+alice.get_pubkey().encode('hex')


ciphertext = alice.encrypt(test, bob.get_pubkey())

print "\n++++Encryption++++"

print "Cipher: "+ciphertext.encode('hex')

print "Decrypt: "+bob.decrypt(ciphertext)

signature = bob.sign("Alice")

print
print "Bob verified: "+ str(pyelliptic.ECC(pubkey=bob.get_pubkey()).verify
(signature, "Alice"))


print "\n++++ECDH++++\n"

print 'Alice:' + alice.get_ecdh_key(bob.get_pubkey()).encode('hex')
print
print 'Bob: '+bob.get_ecdh_key(alice.get_pubkey()).encode('hex')
