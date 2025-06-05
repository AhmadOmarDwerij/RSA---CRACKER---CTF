#  RSA-CTF-Decrypter
## what is RSA
RSA is a type of public-key cryptography used to securely encrypt and decrypt data. It works by using two keys:

  - Public key: Used to encrypt messages. It can be shared with anyone.

  - Private key: Used to decrypt messages. It is kept secret by the owner.

The security of RSA relies on the difficulty of factoring large numbers into primes. The keys are generated from two large prime numbers. Because it’s hard to factor their product, it’s practically impossible for others to derive the private key from the public key.

RSA is widely used for secure communication, digital signatures, and protecting sensitive information online.

## Project overview:
A Python tool to **decrypt RSA-encrypted messages** commonly found in CTF (Capture The Flag) challenges. Supports both **manual input** of primes `p` and `q`, or **automatic factoring** of small `n` values using `sympy`.

> For large `n`, you are encouraged to use [FactorDB](https://factordb.com) or [Integer factorization calculator][(https://www.alpertron.com.ar/ECM.HTM) for factorization.

---

## Features

-  Decrypt RSA ciphertexts with known `e`, `n`, and either:
  - Manually provided primes `p` and `q`
  - Auto-factored small `n` values using `sympy.ntheory.factorint()`
-  Calculates `φ(n)` and the private exponent `d`
-  Converts the decrypted integer back to human-readable string (if decodable)

---

## 📂 Project Structure

```
RSA-CTF-Decrypter/
├── decrypt_rsa.py # Main decryption script
├── README.md # This file
```
---

## Example
```
┌[ahmed][17:22][~]
└$ python3 decrypt_rsa.py
Enter the ciphertext:
2790
Enter the value of n (modulus):
3233
Enter the value of e (public exponent):
17

Choose an option:
1 - Enter p and q manually
0 - Automatically factor n (only for small n)
Enter your choice (0 or 1): 0
Factoring n . This may take a moment...
Found factors:
p = 61
q = 53

Calculated φ(n): 3120
Calculated private exponent d: 2753
Decrypted Message: hi
```

## ⚠️ Notes
sympy.ntheory.factorint() only works on small n. If n is large (as in real RSA), factoring is impractical.
For real RSA CTFs, use FactorDB to obtain p and q.

## Author
Created by Ahmad OMAR DWERIJ for educational and CTF use.
