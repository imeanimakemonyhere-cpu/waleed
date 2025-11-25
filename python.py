import random
import string


chars = string.whitespace + string.punctuation + string.digits + string.ascii_letters
chars = list(chars) 
key = chars.copy()

random.shuffle(key)
                          
while True:                   # encrypt Message:
    plain_text = input("Enter a message to encrypt (q to quit): ")
    if plain_text.upper() == "Q":
        print("GOODBYE....")
        break
    cipher_text = ""

    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]
    
    print(f"Original message : {plain_text}")
    print(f"Original message : {cipher_text}")
                             # decrypt Mesaage:
    cipher_text = input("Enter a message to decrypt: ")
    plain_text = ""

    for letter in cipher_text:
        index = key.index(letter)
        plain_text += chars[index]
    
    print(f"Original message : {cipher_text}")
    print(f"Original message : {plain_text}")
    




