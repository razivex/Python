import os
import ecdsa
import hashlib
import base58

def hash160(data):
    """Applies SHA-256 followed by RIPEMD-160."""
    sha256_hash = hashlib.sha256(data).digest()
    ripemd160_hash = hashlib.new('ripemd160', sha256_hash).digest()
    return ripemd160_hash

private_key_bytes = os.urandom(32)
private_key_hex = private_key_bytes.hex()
print("Private Key:", private_key_hex)

sk = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1)

vk = sk.verifying_key

public_key_bytes_uncompressed = b'\x04' + vk.to_string()
public_key_hex_uncompressed = public_key_bytes_uncompressed.hex()
#print("Uncompressed Public Key:", public_key_hex_uncompressed)

public_key_bytes = vk.to_string()
x_coord = public_key_bytes[:32]
y_coord = public_key_bytes[32:]
prefix = b'\x02' if int.from_bytes(y_coord, 'big') % 2 == 0 else b'\x03'
public_key_bytes_compressed = prefix + x_coord
public_key_hex_compressed = public_key_bytes_compressed.hex()
#print("Compressed Public Key:", public_key_hex_compressed)

public_key_hash = hash160(public_key_bytes_compressed)

network_byte = b'\x00' + public_key_hash

checksum = hashlib.sha256(hashlib.sha256(network_byte).digest()).digest()[:4]

address_bytes = network_byte + checksum

bitcoin_address = base58.b58encode(address_bytes).decode()
print("Bitcoin Address:", bitcoin_address)
