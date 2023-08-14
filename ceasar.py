import random
alphabet = "abcdefghijklmnopqrstuvwxyz"


def encrypt_caesar(original, shift=None):
    if shift is None:
        shift = random.randint(1, 25)

    new = []

    for letter in original:
        if letter.isalpha():
            if letter.islower():
                shifted_index = (alphabet.index(letter) + shift) % 26
                new.append(alphabet[shifted_index])
            else:
                shifted_index = (alphabet.index(letter.lower()) + shift) % 26
                new.append(alphabet[shifted_index].upper())
        else:
            new.append(letter)

    return ["".join(new), shift]


def decrypt_caesar(cipher, shift):
    new = []

    for letter in cipher:
        if letter.isalpha():
            if letter.islower():
                shifted_index = (alphabet.index(letter) - shift) % 26
                new.append(alphabet[shifted_index])
            else:
                shifted_index = (alphabet.index(letter.lower()) - shift) % 26
                new.append(alphabet[shifted_index].upper())
        else:
            new.append(letter)

    return "".join(new)


choice = input(
    "Do you want to encrypt or decrypt using Caesar cipher? (e/d): ")

if choice == "e":
    plain_text = input("Enter the plain text: ")
    encrypted_text, shift = encrypt_caesar(plain_text)
    print("Encrypted text:", encrypted_text)
    print("Shift:", shift)
elif choice == "d":
    shift = int(input("Enter the shift value: "))
    cipher_text = input("Enter the cipher text: ")
    decrypted_text = decrypt_caesar(cipher_text, shift)
    print("Decrypted text:", decrypted_text)
else:
    print("Invalid choice. Please choose 'e' for encrypt or 'd' for decrypt.")