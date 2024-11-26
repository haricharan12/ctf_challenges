import string
import base64
import os

def vigenere_encrypt(text, key):
    alphabet = string.ascii_lowercase
    key = key.lower()
    key_indices = [alphabet.index(k) for k in key if k in alphabet]

    encrypted_text = []
    key_len = len(key_indices)
    i = 0

    for char in text:
        if char in alphabet:
            shift = key_indices[i % key_len]
            encrypted_char = alphabet[(alphabet.index(char) + shift) % 26]
            encrypted_text.append(encrypted_char)
            i += 1
        elif char in string.ascii_uppercase:
            shift = key_indices[i % key_len]
            encrypted_char = alphabet[(alphabet.index(char.lower()) + shift)
                                       % 26].upper()
            encrypted_text.append(encrypted_char)
            i += 1
        else:
            encrypted_text.append(char)

    return ''.join(encrypted_text)

def rot13_encrypt(text):
    result = []
    for char in text:
        if char.isalpha():
            shift = 13
            if char.islower():
                result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
            else:
                result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
        else:
            result.append(char)
    return ''.join(result)

def base64_encode(text):
    encoded_bytes = base64.b64encode(text.encode())
    return encoded_bytes.decode()

def generate_challenge(flag, vigenere_key):
    vigenere_encoded = vigenere_encrypt(flag, vigenere_key)
    rot13_encoded = rot13_encrypt(vigenere_encoded)
    final_encoded = base64_encode(rot13_encoded)

    return final_encoded

def main():
    # Read the dynamically generated flag from the setup
    try:
        with open("flag.txt", "r") as f:
            flag = f.read().strip()
    except FileNotFoundError:
        print("Error: flag.txt not found. Please ensure setup-challenge.py is executed first.")
        return

    # Define the Vigenère cipher key
    vigenere_key = "CarlFriedrichGauss"

    # Generate the encoded challenge
    encoded_challenge = generate_challenge(flag, vigenere_key)
    print("Encoded Challenge:", flush=True)
    print(encoded_challenge)
    print("\nFollow the order and you can decrypt me"
          "\n1. It's pretty simple decoding."
          "\n2. I think you should f1gur3 this out on your own."
          "\n3. Giovan Battista Bellaso"
          "\nAuthor of the Key = 0.01720209895 [This is not the key!!!]")

if __name__ == "__main__":
    main()
