This script contains the functional implementations of various encryption and decryption algorithms discussed in the project, ranging from transposition methods to bitwise stream operations.

```python
import math
import string

# =============================================================================
# I. COLUMNAR TRANSPOSITION CIPHER
# =============================================================================
# This cipher involves writing the plaintext in a grid and reading it out 
# column-wise based on the alphabetical order of the keyword.

def columnar_encrypt(msg, key):
    """
    Encrypts a message using the Columnar Transposition method.
    """
    cipher = ""
    k_indx = 0
    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = sorted(list(key)) # Alphabetical order for column reading

    col = len(key)
    # Calculate number of rows required in the grid
    row = int(math.ceil(msg_len / col))

    # Padding: Fill empty cells with '_' to complete the matrix
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)

    # Create the matrix: map characters into row-wise blocks
    matrix = [msg_lst[i: i + col] for i in range(0, len(msg_lst), col)]

    # Read columns based on alphabetical priority of key letters
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx] for row in matrix])
        k_indx += 1

    return cipher

def columnar_decrypt(cipher, key):
    """
    Decrypts a message by reconstructing the grid and reading row-wise.
    """
    msg = ""
    k_indx = 0
    msg_indx = 0
    msg_len = float(len(cipher))
    msg_lst = list(cipher)

    col = len(key)
    row = int(math.ceil(msg_len / col))
    key_lst = sorted(list(key))

    # Create an empty matrix to fill column-wise
    dec_cipher = []
    for _ in range(row):
        dec_cipher.append([None] * col)

    # Fill the matrix column by column based on key order
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1

    # Convert matrix back to string and remove padding
    msg = ''.join(sum(dec_cipher, []))
    return msg.strip('_')

# =============================================================================
# II. STREAM CIPHER LOGIC
# =============================================================================
# Stream ciphers work by XORing plaintext bits with a pseudorandom keystream.

def text_to_bits(text):
    """Helper: Converts string to a string of bits (binary)."""
    bits = bin(int.from_bytes(text.encode(), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def bits_to_text(bits):
    """Helper: Converts string of bits back to a string."""
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

def stream_xor(plaintext_bits, keystream_bits):
    """
    Performs a bitwise XOR between the plaintext and the keystream.
    Encryption and Decryption use the same XOR logic.
    """
    cipher_bits = ""
    # zip() ensures we only iterate as long as the shortest input
    for p, k in zip(plaintext_bits, keystream_bits):
        # XOR logic: 1 if bits differ, 0 if they are the same
        res = int(p) ^ int(k)
        cipher_bits += str(res)
    return cipher_bits

# =============================================================================
# EXAMPLE EXECUTION
# =============================================================================
if __name__ == "__main__":
    # Test Columnar Transposition
    msg = "Geeks for Geeks"
    key = "HACK"
    encrypted_ct = columnar_encrypt(msg, key)
    print(f"Columnar Encrypted: {encrypted_ct}")
    print(f"Columnar Decrypted: {columnar_decrypt(encrypted_ct, key)}")

    # Test Stream Cipher
    plaintext = "Hi"
    p_bits = text_to_bits(plaintext)
    # In a real scenario, the keystream must be truly random and same length
    keystream = "1010101011110000" 
    encrypted_bits = stream_xor(p_bits, keystream)
    print(f"Stream Encrypted (bits): {encrypted_bits}")
    decrypted_bits = stream_xor(encrypted_bits, keystream)
    print(f"Stream Decrypted (text): {bits_to_text(decrypted_bits)}")

```

### Detailed Breakdown of Implementation:

1. **Columnar Transposition Logic**:
* **Padding**: Crucial for forming a perfect rectangle. The `math.ceil` function ensures we have enough rows to accommodate the message length divided by the key width.
* **Alphabetical Sorting**: The line `sorted(list(key))` is the "engine" of the cipher. It determines the sequence in which columns are extracted. For a key "HACK", the order is A(1), C(2), H(3), K(4).


2. **Stream Cipher Logic**:
* **The XOR Principle**: This is the heart of modern stream encryption. The property  means the same function `stream_xor` is used for both encryption and decryption.
* **Bit-by-Bit Processing**: Unlike block ciphers, this function processes individual bits. In the report, this simulates how high-speed hardware encryption works.
* **Binary Conversion**: Added `text_to_bits` and `bits_to_text` so the code can handle real-world string data instead of just 0s and 1s.
