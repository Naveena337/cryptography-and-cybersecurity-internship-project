This document presents the **mathematical foundations, formulas, and step-by-step algorithms** for the cryptographic techniques studied and implemented as part of this cybersecurity internship project.

## I. RSA Cryptosystem

RSA is an asymmetric (public-key) cryptosystem whose security relies on the difficulty of factoring large prime numbers.

### Key Generation

1. Choose two large prime numbers:

$$
p,; q
$$

2. Compute the modulus:

$$
n = p \times q
$$

3. Compute Euler’s Totient Function:

$$
\phi(n) = (p - 1)(q - 1)
$$

4. Choose an integer ( e ) such that:

$$
1 < e < \phi(n), \quad \gcd(e,\phi(n)) = 1
$$

5. Compute the private key ( d ):

$$
d \equiv e^{-1} \pmod{\phi(n)}
$$

### Encryption

Plaintext message ( M ) is encrypted as:

$$
C = M^e \bmod n
$$

### Decryption

Ciphertext ( C ) is decrypted as:

$$
M = C^d \bmod n
$$

### Example

* **Public Key:** ( (e, n) )
* **Private Key:** ( (d, n) )
* **Encryption:**
  $$
  C = M^e \bmod n
  $$
* **Decryption:**
  $$
  M = C^d \bmod n
  $$

## II. ElGamal Cryptosystem

ElGamal is an asymmetric cryptosystem based on the **Discrete Logarithm Problem**.

### Key Generation

1. Choose a large prime ( p ) and generator ( g )
2. Select a private key ( x ), where:

$$
1 < x < p - 1
$$

3. Compute:

$$
y = g^x \bmod p
$$

* **Public Key:** ( (p, g, y) )
* **Private Key:** ( x )

### Encryption

1. Choose random integer ( k )
2. Compute:

$$
C_1 = g^k \bmod p
$$

3. Compute:

$$
C_2 = M \cdot y^k \bmod p
$$

* **Ciphertext:** ( (C_1, C_2) )

### Decryption

Recover plaintext:

$$
M = C_2 \cdot (C_1^x)^{-1} \bmod p
$$

## III. Feistel Cipher Algorithm

Feistel structure forms the basis of many block ciphers such as DES.

### Algorithm Steps

1. Divide plaintext into two halves:
   $$
   L_0,; R_0
   $$

2. For each round ( i ):

$$
L_i = R_{i-1}
$$

$$
R_i = L_{i-1} \oplus F(R_{i-1}, K_i)
$$

3. Final ciphertext:

$$
C = L_n | R_n
$$

### Example

* **Plaintext:** `"Hello"`
* **Process:** Binary conversion → XOR with round keys → recombination
* **Ciphertext:** `"E1!w("`

## IV. Substitution Cipher (Modular Arithmetic)

Each letter is replaced by another letter using modular arithmetic.

### Letter Mapping

$$
A = 0,; B = 1,; \dots,; Z = 25
$$


### Encryption

$$
E(x) = (x + k) \bmod 26
$$

### Decryption

$$
D(x) = (x - k) \bmod 26
$$

### Example

* **Plaintext:** `I am studying Data Encryption`
* **Key:** ( k = 4 )

**Conversions:**

* ( I (8) + 4 = M (12) )
* ( a (0) + 4 = e (4) )
* ( m (12) + 4 = q (16) )

**Ciphertext:**
M eq wxyhCmrk Hexe IrgvCtxmsr

## V. Columnar Transposition Cipher

A transposition cipher that rearranges characters based on a keyword.

### Algorithm Steps

1. Choose a keyword of length ( n )
2. Write plaintext row-wise in a grid of ( n ) columns
3. Number columns by alphabetical order of keyword
4. Read columns in numerical order
### Example

* **Plaintext:** `Geeks for Geeks`
* **Keyword:** `HACK`

| H (3) | A (1) | C (2) | K (4) |
| ----- | ----- | ----- | ----- |
| G     | e     | e     | k     |
| s     | _     | f     | o     |
| r     | _     | G     | e     |
| e     | k     | s     | _     |

**Ciphertext:**

```
e__kefGsGsrekoe_
```

## VI. Permutation Cipher

A block-based transposition cipher using a fixed permutation.

### Algorithm Steps

1. Divide plaintext into blocks of size ( n )
2. Define permutation ( \pi )
3. Rearrange characters per block
4. Read across rows

### Example

* **Plaintext:** `COMPUTER`
* **Block size:** ( n = 4 )
* **Permutation:** ( \pi = (3,4,2,1) )

**Block 1:** `COMP → PMCO`
**Block 2:** `UTER → REUT`

**Ciphertext:**

```
PMCOREUT
```

---

## VII. Elliptic Curve Cryptography (ECC)

ECC is an asymmetric cryptosystem based on elliptic curve algebra.

### Elliptic Curve Equation

$$
y^2 = x^3 + ax + b
$$
<img width="3999" height="2203" alt="image" src="https://github.com/user-attachments/assets/3bb3507f-b3eb-4e18-8011-e49c02a2e55c" />
Where:

$$
4a^3 + 27b^2 \neq 0
$$

### Key Concepts

* **Private Key:** ( d )
* **Public Key:**
 Q = d · G
* **Security Basis:** Elliptic Curve Discrete Logarithm Problem (ECDLP)

## VIII. Stream Cipher Logic

Stream ciphers encrypt data bit-by-bit using a pseudorandom keystream.

### Mathematical Model

1. Keystream generator produces:

$$
K = k_1, k_2, k_3, \dots
$$

2. Encryption:

$$
C_i = P_i \oplus K_i
$$

### Key Feature

The same plaintext bit produces **different ciphertext bits** when the keystream varies.
