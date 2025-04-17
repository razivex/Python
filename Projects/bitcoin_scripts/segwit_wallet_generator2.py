import os
import hashlib
import base58
import ecdsa
import bech32

private_key = os.urandom(32)
private_key_hex = private_key.hex()

sk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
vk = sk.get_verifying_key()
public_key = b'\x02' + vk.to_string()[:32] if vk.to_string()[63] % 2 == 0 else b'\x03' + vk.to_string()[:32]

sha256_pk = hashlib.sha256(public_key).digest()
ripemd160_pk = hashlib.new('ripemd160', sha256_pk).digest()

witness_version = 0
witness_program = ripemd160_pk
address = bech32.encode('bc', witness_version, witness_program)

extended_key = b'\x80' + private_key
extended_key += b'\x01'
checksum = hashlib.sha256(hashlib.sha256(extended_key).digest()).digest()[:4]
wif = base58.b58encode(extended_key + checksum).decode()

print("Private Key:", wif)
print("Bitcoin Address:", address)
