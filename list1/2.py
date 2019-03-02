from hashlib import md5, sha1, sha3_512
from time import time
from Crypto.Protocol.KDF import PBKDF2

def test_hash(fun, iters, text):
    t = time()
    for i in range(iters):
        fun(text)
    print(f"Running {iters} iterations took {time()-t}")


text = b'Ala ma kota, a kot ma ale' * 1313
iters = 100

# regular hashes

for name, fun in [('md5', md5), ('sha1', sha1), ('sha3', sha3_512)]:
    print('')
    print(f"{name}:")
    test_hash(fun, iters, text)

# slow function

salt = b"kind of salt"
password = b"very tajne"
slow_iters = 1

print('')
print('PBKDF2:')
t = time()
for _ in range(iters):
    PBKDF2(password, salt)
print(f"Running {slow_iters} iterations took {time()-t}")
