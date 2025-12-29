Code:
# Python program to illustrate Rail Fence Cipher Encryption and Decryption

def encryptRailFence(text, key):
    rail = [['\n' for i in range(len(text))]
            for j in range(key)]
    
    dir_down = False
    row, col = 0, 0
    
    for i in range(len(text)):
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
        
        rail[row][col] = text[i]
        col += 1
        
        if dir_down:
            row += 1
        else:
            row -= 1
            
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return "".join(result)

def decryptRailFence(cipher, key):
    rail = [['\n' for i in range(len(cipher))]
            for j in range(key)]
    
    dir_down = None
    row, col = 0, 0
    
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        
        rail[row][col] = '*'
        col += 1
        
        if dir_down:
            row += 1
        else:
            row -= 1
            
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1
                
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
            
        if (rail[row][col] != '\n'):
            result.append(rail[row][col])
            col += 1
            
        if dir_down:
            row += 1
        else:
            row -= 1
    return "".join(result)

if __name__ == "__main__":
    # Test 1: Using "RAILFENCE"
    text1 = "RAILFENCE"
    key1 = 2
    enc1 = encryptRailFence(text1, key1)
    print(f"Original: {text1}")
    print(f"Encrypted (Key {key1}): {enc1}")
    print(f"Decrypted: {decryptRailFence(enc1, key1)}")
    
    print("-" * 30)

    # Test 2: Using "CYBERSECURITY"
    text2 = "CYBERSECURITY"
    key2 = 3
    enc2 = encryptRailFence(text2, key2)
    print(f"Original: {text2}")
    print(f"Encrypted (Key {key2}): {enc2}")
    print(f"Decrypted: {decryptRailFence(enc2, key2)}")
Output:
Original: RAILFENCE
Encrypted (Key 2): RIFNEALEC
Decrypted: RAILFENCE
------------------------------
Original: CYBERSECURITY
Encrypted (Key 3): CRUYYESCRTB EI
Decrypted: CYBERSECURITY
