"""
Build a system where when user enters Reference ID it is encrypted,
so that hackers cannot view the mapping of Reference ID and finger print.
1.Read the input from command line –Reference ID
2.Check for validity –it should be 12 digits and allows on number and alphabet
3.Encrypt the Reference ID and print it for reference

Enhancements for code:
1.Allow some special characters in ReferenceID
2.Give the option for decryption to user
"""

from cryptography.fernet import Fernet


def save_key():
    # Generates a key and save it into a file
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    # Load the previously generated key
    return open("secret.key", "rb").read()


def generate_key():
    try:
        key = load_key()
    except FileNotFoundError:
        save_key()
        key = load_key()

    return Fernet(key)


def encrypt_me(message) -> object:
    return generate_key().encrypt(message.encode())


def decrypt_me(encrypted_message):
    return generate_key().decrypt(encrypted_message).decode()


def isValid(reference_id):
    if len(reference_id) == 12:
        alphanum = 0
        special = 0
        for i in reference_id:
            if i.isalnum():
                alphanum += 1
            else:
                special += 1

        if 0 in (alphanum, special):
            return False
        else:
            return True
    return False


def user_input():
    ref_id = input("Enter reference Id: ")
    if isValid(ref_id):

        encrypted = encrypt_me(ref_id)
        print("Encrypted value is: ", encrypted)

        response = input("Do you want to decrypt? ")
        if response.upper() in ('Y', 'YES', 'TRUE'):
            print("Decrypted value is: ", decrypt_me(encrypted))
        print("Thank you!!")

    else:
        print("Wrong information entered...")
        user_input()


if __name__ == "__main__":
    user_input()
