# This program defines two functions, encrypt and decrypt, 
# that take a plaintext or ciphertext string and a shift value as inputs. 
# The encrypt function iterates through each character in the plaintext, 
# shifting its ASCII value by the shift amount (mod 26), and appending the 
# shifted character to the ciphertext string. Similarly, the decrypt function 
# iterates through each character in the ciphertext, shifting its ASCII value 
# by the negative of the shift amount (mod 26), and appending the shifted character 
# to the plaintext string.
#aThis program encrypts/decrypts only lowercase letters,
#  if you want to encrypt/decrypt uppercase letters and other symbols you 
#  will have to add them to the condition of the isalpha() method

def encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                shifted_char = chr(((ord(char) - 97 + shift) % 26) + 97)
            else:  # Uppercase
                shifted_char = chr(((ord(char) - 65 + shift) % 26) + 65)
        elif char.isdigit():
            shifted_char = str((int(char) + shift) % 10)  # Handle digits
        else:
            shifted_char = char
        ciphertext += shifted_char
    return ciphertext

def decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                shifted_char = chr(((ord(char) - 97 - shift) % 26) + 97)
            else:  # Uppercase
                shifted_char = chr(((ord(char) - 65 - shift) % 26) + 65)
        elif char.isdigit():
            shifted_char = str((int(char) - shift) % 10)  # Handle digits
        else:
            shifted_char = char
        plaintext += shifted_char
    return plaintext

# Test case
plaintext = input("Enter plain text:")
shift = int(input("Enter the shift:"))
ciphertext = encrypt(plaintext, shift)
print("Ciphertext:", ciphertext)
decrypted_plaintext = decrypt(ciphertext, shift)
print("Decrypted plaintext:", decrypted_plaintext)

