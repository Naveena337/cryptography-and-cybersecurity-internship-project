To provide a comprehensive foundation for your `cipher_theory.md` file, the following sections elaborate on the core concepts derived from the project report, covering definitions, key categorizations, transformation methods, and processing types.

### **1. Detailed Definition of a Cipher**

A **cipher** is a specific algorithm used in cryptology to perform both encryption and its corresponding decryption. It is essentially a set of clearly defined steps applied to data to transform legible **plaintext** into **ciphertext**, which appears as random, unreadable information to anyone without the proper key.
**Purpose:** Ciphers are the cornerstone of modern digital security, used in technologies like the internet (HTTPS/TLS), mobile phones, digital television, and ATMs to maintain confidentiality and privacy.
**The Key's Role:** In practical applications, the security of a cipher relies on keeping the **key** secret rather than the algorithm itself. Modern implementations recommend keys of at least **128 bits** to remain resilient against brute-force attacks.

### **2. Key Categorization: Symmetric vs. Asymmetric**

Ciphers are primarily categorized by how their keys are managed and used during the cryptographic process.

#### **Symmetric Key Cryptography (Private Key)**

In this system, the **same secret key** is used for both encryption and decryption.

**Advantages:** It is computationally faster than asymmetric methods and is ideal for encrypting large volumes of data transmissions.

**Challenges:** The primary difficulty is **key management**—the secret key must be shared securely between parties without being intercepted.

**Examples:** Digital Encryption Standard (DES), Advanced Encryption Standard (AES), and International Data Encryption Algorithm (IDEA).

#### **Asymmetric Key Cryptography (Public Key)**

This is a newer concept that uses a **pair of mathematically related keys**: a Public Key and a Private Key. 
**Mechanism:** The Public Key is used by the sender to encrypt data and can be openly published. Only the recipient's corresponding Private Key, which is kept secret, can decrypt that data.

**Security Principle:** While the two keys are mathematically linked, it is computationally infeasible to derive the private key from the public key.

**Examples:** RSA Cryptosystem, ElGamal, and Elliptic Curve Cryptography (ECC).

### **3. Transformation Methods: Substitution vs. Transposition**

These are the two basic forms of data transformation used to obscure information.

#### **Substitution Ciphers**

These ciphers replace specific bits, characters, or blocks of data with alternative sequences while maintaining the original order.

**Monoalphabetic:** Uses a single fixed alphabet for the entire message (e.g., if 'A' is replaced by 'K', it remains 'K' throughout).

**Polyalphabetic:** Uses a more complex, mixed alphabet where a single character might be represented by different characters at different points in the message.

**Example:** The **Caesar Cipher**, where each letter is shifted by a fixed number of positions (typically 3) in the alphabet.

#### **Transposition Ciphers**

Unlike substitution, transposition keeps all the original bits of data but **rearranges their order** according to a specific algorithm.

**Mechanism:** For example, in a **Columnar Transposition**, the plaintext is written out in rows of a fixed length and then read off column by column in a scrambled order defined by a keyword.

 
**Characteristics:** These can be more difficult and error-prone to implement manually compared to simple substitution ciphers.

### **4. Processing Types: Block vs. Stream Ciphers**

Ciphers are also classified based on the "chunk" size of data they process at one time.

#### **Block Ciphers**

These group plaintext symbols into **fixed-size blocks** (e.g., 64 or 128 bits) and process the entire block simultaneously.
**Padding:** Since plaintext is rarely an exact multiple of the block size, "redundant bits" (padding) are added to the final block to reach the required size.

**Strength:** Their security depends primarily on the key length rather than the block size itself.

#### **Stream Ciphers**

These process data as a continuous stream, encrypting **one bit or one byte at a time**.

**Mechanism:** They use a pseudorandom bit generator to produce a **keystream**, which is then XORed bit-by-bit with the plaintext to create the ciphertext.
**Advantages:** They are generally easier to implement with fewer lines of code and are highly effective for securing real-time data streams over networks.
