CODE: 
# Python Program for Decoding the String 
# using Classical Cipher 
import string 
  
# stores all upper case alphabets 
all_alphabets = list(string.ascii_uppercase) 
  
keyword = "Star War" 
keyword1 = keyword.upper() 
ciphertext = "SPPSAG SP RSVJ" 
  
  
# converts message to list 
ct = [] 
for i in ciphertext: 
    ct.append(i.upper()) 
  
# removes default elements 
  
  
def duplicates(list): 
    key = [] 
    for i in list: 
                             
        if i not in key: 
            key.append(i) 
  
    return key 
  
  
keyword1 = duplicates(keyword1) 
  
# Stores the encryption list 
encrypting = duplicates(keyword1+all_alphabets) 
  
# removes spaces from the encryption list 
for i in encrypting: 
    if(i == ' '): 
        encrypting.remove(' ') 
  
# maps each element of the message to the encryption list and stores it 
in ciphertext 
message = "" 
for i in range(len(ct)): 
    if(ct[i] != ' '): 
        message = message+all_alphabets[encrypting.index(ct[i])] 
    else: 
        message = message+' ' 
  
print("Keyword : ", keyword) 
print("Ciphered Text : ", ciphertext) 
print("Message before Ciphering : ", message) 
 
OUTPUT: 
('Keyword : ', 'Star War') 
('Ciphered Text : ', 'SPPSAG SP RSVJ') 
('Message before Ciphering : ', 'ATTACK AT DAWN')
