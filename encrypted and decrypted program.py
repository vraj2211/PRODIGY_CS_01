def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Caesar Cipher Program")
    choice = input("Do you want to encrypt or decrypt the message? (enter 'encrypt' or 'decrypt'): ").strip().lower()
    
    if choice not in ['encrypt', 'decrypt']:
        print("Invalid choice! Please enter 'encrypt' or 'decrypt'.")
        return
    
    message = input("Enter the message: ").strip()

    try:
        shift = int(input("Enter the shift value: ").strip())
    except ValueError:
        print("Invalid shift value! shift value must be in integer")
        return
    
    if choice == 'encrypt':
        result = caesar_cipher_encrypt(message, shift)
        print(f"Encrypted message: {result}")
    else:
        result = caesar_cipher_decrypt(message, shift)
        print(f"Decrypted message: {result}")

if __name__ == "__main__":
    main()
input("Press Enter to exit...")

