encrypt & decrypt messages>:::

import random
import string

class CipherEncryptor:
    """Simple substitution cipher for encryption/decryption."""
    
    def __init__(self):
        self.chars = list(string.whitespace + string.punctuation + string.digits + string.ascii_letters)
        self.key = self.chars.copy()
        random.shuffle(self.key)
    
    def encrypt(self, plain_text: str) -> str:
        """Encrypt a message."""
        cipher_text = ""
        for letter in plain_text:
            if letter in self.chars:
                index = self.chars.index(letter)
                cipher_text += self.key[index]
            else:
                cipher_text += letter  # Keep unknown chars
        return cipher_text
    
    def decrypt(self, cipher_text: str) -> str:
        """Decrypt a message."""
        plain_text = ""
        for letter in cipher_text:
            if letter in self.key:
                index = self.key.index(letter)
                plain_text += self.chars[index]
            else:
                plain_text += letter  # Keep unknown chars
        return plain_text
    
    def display_key(self) -> None:
        """Display the cipher key (for debugging)."""
        print("\n📋 Cipher Key:")
        print(f"Original: {''.join(self.chars)}")
        print(f"Shuffled: {''.join(self.key)}\n")

def main():
    """Main program loop."""
    print("🔐 Welcome to the Cipher Encryptor!\n")
    cipher = CipherEncryptor()
    
    while True:
        print("Options:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. View cipher key")
        print("4. Quit")
        
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == "1":
            plain_text = input("Enter a message to encrypt: ")
            encrypted = cipher.encrypt(plain_text)
            print(f"✉️  Original:  {plain_text}")
            print(f"🔒 Encrypted: {encrypted}\n")
        
        elif choice == "2":
            cipher_text = input("Enter a message to decrypt: ")
            decrypted = cipher.decrypt(cipher_text)
            print(f"🔒 Encrypted: {cipher_text}")
            print(f"✉️  Decrypted: {decrypted}\n")
        
        elif choice == "3":
            cipher.display_key()
        
        elif choice == "4":
            print("GOODBYE! 👋")
            break
        
        else:
            print("❌ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
