from sympy.ntheory import factorint

print("Enter the ciphertext:")
cyphertext = int(input())

print("Enter the value of n (modulus):")
n = int(input())

print("Enter the value of e (public exponent):")
e = int(input())

# Ask user to choose method of factoring
print("\nChoose an option:")
print("1 - Enter p and q manually")
print("0 - Automatically factor n (only for small n)")
print("Note: For large 'n', try using https://factordb.com to factor it easily.")
choice = input("Enter your choice (0 or 1): ").strip()

# Get or calculate p and q
if choice == "1":
    p = int(input("Enter the value of p (prime 1): "))
    q = int(input("Enter the value of q (prime 2): "))
elif choice == "0":
    print("Factoring n . This may take a moment...")
    factors = factorint(n)
    if len(factors) == 2:
        p, q = list(factors.keys())
        print(f"Found factors:\np = {p}\nq = {q}")
    else:
        print("Failed to factor n automatically. Exiting.")
        exit(1)
else:
    print("Invalid choice. Exiting.")
    exit(1)

# Compute phi(n)
phi = (p - 1) * (q - 1)
print("\nCalculated φ(n):", phi)

# Modular inverse function
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Calculate private key d
d = mod_inverse(e, phi)
print("Calculated private exponent d:", d)

# Decrypt ciphertext
M = pow(cyphertext, d, n)

# Convert integer to bytes, then decode
Message_bytes = M.to_bytes((M.bit_length() + 7) // 8, 'big')
try:
    Message = Message_bytes.decode()
except UnicodeDecodeError:
    Message = Message_bytes  # If decoding fails, show raw bytes

print("Decrypted Message:", Message)
