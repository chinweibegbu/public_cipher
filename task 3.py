import random
from typing import Tuple

# Find n^k % p
def mod_calcualtion(n: int, k: int, p: int):
    if k == 0:
        return 1
    tmp = mod_calcualtion(n, k // 2, p) ** 2
    if k % 2 == 0:
        return tmp % p
    else: 
        return tmp * n % p


# Check if a given number is prime
def is_prime(num, bases=None):
    if bases is None:
        bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 31]
    for base in bases:
        if mod_calcualtion(base, num, num) != base:
            return False
    return True

# Generate a prime number with a given length in base 2
def generate_prime(length):
    assert length >= 5
    start = 1 << length
    end = 1 << (length + 1)
    while True:
        num = random.randint(start, end - 1)
        if is_prime(num):
            return num

# Generate n = p * q === (n, phi(n))
def generate_n_and_phi_n(size):
    p, q = generate_prime(size // 2), generate_prime(size // 2 - 2)
    return p * q, (p - 1) * (q - 1)


# Find the solution of ax + by = gcd(x, y) === (x, y, gcd(x, y))
def extended_gcd(a, b):
    if b == 0:
        return 1, 0, a
    x, y, gcd = extended_gcd(b, a % b)
    return y, x - (a // b) * y, gcd

# Generate keys, returns (e, d, n), where e is the public key and d is the private key.
def generate_keys(size: int = 512):
    n, phi_n = generate_n_and_phi_n(size)
    e = generate_prime(size // 2)
    d, _, _ = extended_gcd(e, phi_n)
    if d < 0:
        d += phi_n
    return e, d, n

# Encrypt a text with a public key and n
def encrypt(text, public_key, n):
    return mod_calcualtion(text, public_key, n)

# Decrypt a text with a private key and n
def decrypt(ciphertext, private_key, n):
    return mod_calcualtion(ciphertext, private_key, n)


# Testing
print("Generate keys:")
public_key, private_key, n = generate_keys()
print(f"public key: {public_key}")
print(f"private key: {private_key}")
print(f"n: {n}\n\n")

text = 123456789
print(f"Encrypting text {text}:")
ciphertext = encrypt(text, public_key, n)
print(f"ciphertext {ciphertext}:\n\n")

print(f"Decrypting text {ciphertext}:")
decrypted_text = decrypt(ciphertext, private_key, n)
print(f"Original text {decrypted_text}\n\n")