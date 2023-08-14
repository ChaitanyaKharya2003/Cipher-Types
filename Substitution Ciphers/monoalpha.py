import random

alphabet = "abcdefghijklmnopqrstuvwxyz"


def encrypt(original, key=None):
    if key is None:
            l = list(alphabet)
            random.shuffle(l)
            key = "".join(l)

    new = []

    for letter in original:
        if letter.isalpha():
            if letter.islower():
                new.append(key[alphabet.index(letter)])
            else:
                new.append(key[alphabet.index(letter.lower())].upper())
        else:
            new.append(letter)

    return ["".join(new), key]


def decrypt(cipher, key):
    new = []
    for letter in cipher:
        if letter.isalpha():
            if letter.islower():
                new.append(alphabet[key.index(letter)])
            else:
                new.append(alphabet[key.index(letter.lower())].upper())
        else:
            new.append(letter)

    return "".join(new)


choice = input("Do you want to encrypt or decrypt? (e/d): ")

if choice == "e":
    plain_text = input("Enter the plain text: ")
    encrypted_text, key = encrypt(plain_text)
    print("Cypher text:", encrypted_text)
    print("Key:", key)
elif choice == "d":
    key = input("Enter the key: ")
    cipher_text = input("Enter the cipher text: ")
    decrypted_text = decrypt(cipher_text, key)
    print("Decrypted text:", decrypted_text)
else:
    print("Invalid choice. Please choose 'e' for encrypt or 'd' for decrypt.")