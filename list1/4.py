from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA384

def sign(data, private_key):
    signer = PKCS1_v1_5.new(private_key)
    data_hash = SHA384.new(data)
    return signer.sign(data_hash)

def verify(data, public_key, signature):
    verifier = PKCS1_v1_5.new(public_key)
    data_hash = SHA384.new(data)
    try:
        verifier.verify(data_hash, signature)
        return True
    except (ValueError):
        return False
    

data = b'ala ma kota, a kot ma ale' * 1313
key_length = 2048

private_key = RSA.generate(key_length)
public_key = private_key.publickey()

signature = sign(data, private_key)

is_valid = verify(data, public_key, signature)

print(is_valid)