from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto import Random
from time import time

print("")
print("AES")
print("")

key128 = b'Sixteen byte key'
key192 = b'123456789012345678901234'
key256 = b'12345678901234567890123456789012'

keys = [key128, key192, key256]
mode = AES.MODE_CBC
iv = Random.new().read(AES.block_size)

# aes_message = b'Random message... ' * 1000
aes_message = b'ala ' * 32

aes_runs = 1000

for key in keys:
    t1 = time()
    for _ in range(aes_runs):
        cipher = AES.new(key, mode, iv)
        cipher.encrypt(aes_message)
    print("For key with length", len(key), 'it took', time()-t1, 'to run AES', aes_runs, 'times')

#################################################################
print("")
print("RSA")
print("")

rsa_key_lengths = [1024 * x for x in range(1, 5)]

rsas = list(map(RSA.generate, rsa_key_lengths))
rsa_runs = 1000

rsa_message = b'ala ' * 32

for rsa in rsas:
    t1 = time()
    for _ in range(rsa_runs):
        rsa.encrypt(rsa_message, b'')
    print("For key with length", rsa.size()+1, 'it took', time()-t1, 'to run RSA', rsa_runs, 'times')