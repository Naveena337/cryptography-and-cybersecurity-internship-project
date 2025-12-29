To ensure your GitHub repository looks professional and renders all mathematical formulas correctly, you should use **Markdown** syntax. GitHub supports LaTeX-style formulas using the `$` and `$$` delimiters.

Below is the complete, formatted content for your `formulas_and_algorithms.md` file. You can copy and paste this directly.

---

# 2. formulas_and_algorithms.md

This file provides the mathematical logic and step-by-step procedures for the ciphers implemented in this project.

## I. RSA Cryptosystem

RSA is a widely used asymmetric (public-key) cryptosystem based on the mathematical difficulty of factoring large prime numbers.

### Key Generation Steps

1. Choose two large prime numbers,  and .
2. Compute . This  is used as the modulus for both public and private keys.
3. Compute Euler's totient function, .
4. Choose an integer  such that  and  is co-prime to .
5. Determine  as the modular multiplicative inverse of  (i.e., ).

### Encryption

Transform plaintext  (represented as a number less than ) into ciphertext :


### Decryption

Recover the original plaintext  from ciphertext  using the private key :


### Example

* **Setup:** Given a public key pair  and a private key .
* **Encryption:** To encrypt plaintext :


* **Decryption:** To decrypt ciphertext :



---

## II. ElGamal Cryptosystem

The ElGamal system is an asymmetric algorithm based on the Discrete Logarithm Problem.

### Key Generation

1. Select a large prime  and a generator .
2. Choose a private key  (where ).
3. Compute .
4. The **Public Key** is  and the **Private Key** is .

### Encryption

1. Generate a random number .
2. Compute .
3. Compute .
4. The ciphertext is the pair .

### Decryption

1. Compute the decryption factor: .
2. Recover plaintext: .

---

## III. Feistel Cipher Algorithm

The Feistel structure is a design used for many block ciphers, such as DES. It uses multiple rounds of substitution and permutation.

### Algorithm Steps

1. **Divide:** Convert plaintext to 8-bit binary and divide it into two halves: Left () and Right ().
2. **Round 1:**
* Generate .
* .
* .


3. **Round 2:**
* Generate .
* .
* .


4. **Final Step:** Concatenate  and  to form the ciphertext.

### Example

* **Plaintext:** "Hello"
* **Ciphertext:** "E1!w("
* **Process:** The text is converted to binary, split, XORed with random keys across two rounds, and then converted back to characters.

---

## IV. Substitution Cipher (Modular Arithmetic)

This cipher replaces each character in the plaintext with another character based on a fixed shift key.

### Mathematical Mapping

Assign numbers to letters: .

### Encryption ()

### Decryption ()

### Example

* **Plaintext:** "I am studying Data Encryption"
* **Key:** 4
* **Encryption Process:**
* 'I' (index 8) + 4 = 12 ('M')
* 'a' (index 0) + 4 = 4 ('e')
* 'm' (index 12) + 4 = 16 ('q')


* **Output Ciphertext:** "M eq wxyhCmrk Hexe IrgvCtxmsr"

---

## V. Additional Ciphers

### Columnar Transposition

A transposition cipher where the message is written in rows and read in columns based on a keyword.

1. **Write:** Fill the message into a grid of width  (length of keyword).
2. **Sort:** Arrange columns alphabetically based on the keyword.
3. **Read:** Read the characters column by column to form the ciphertext.

### Permutation Cipher

Unlike Columnar Transposition, the Permutation cipher:

1. Splits plaintext into segments of size .
2. Reorders characters within each segment based on a mathematical permutation .
3. Reads the results **across the rows** rather than columns.
