# Python code to implement Vigenere Cipher

# This function generates the key in a cyclic manner
# until its length equals the length of the original text
def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return "".join(key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

# This function returns the encrypted text
def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return "".join(cipher_text)

# This function decrypts the encrypted text
def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return "".join(orig_text)

# Driver code
if __name__ == "__main__":
    string = "CYBERSECURITY"
    keyword = "AYUSH"

    key = generateKey(string, keyword)
    cipher_text = cipherText(string, key)

    print("Ciphertext :", cipher_text)
    print("Original/Decrypted Text :", originalText(cipher_text, key))
Output:
Ciphertext : CWCYJYWCFYGL
Original/Decrypted Text : CYBERSECURITY

