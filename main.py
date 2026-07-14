from cryptography.fernet import Fernet
import re
import random
from datetime import datetime

# =========================
# Caesar Cipher Functions
# =========================

def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


# =========================
# AES Functions
# =========================

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as file:
        file.write(key)
    return key


def load_key():
    with open("secret.key", "rb") as file:
        return file.read()


def aes_encrypt(text, key):
    f = Fernet(key)
    return f.encrypt(text.encode())


def aes_decrypt(cipher_text, key):
    f = Fernet(key)
    return f.decrypt(cipher_text).decode()


# =========================
# Password Strength Checker
# =========================

def check_password_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"\d", password):
        score += 1

    if re.search(r"[!@#$%^&*()_+=-]", password):
        score += 1

    if score <= 2:
        return "🔴 Weak Password"

    elif score <= 4:
        return "🟡 Medium Password"

    else:
        return "🟢 Strong Password"
 # =========================
# History Function
# =========================

def save_history(feature, operation, input_data, output_data):
    with open("history.txt", "a") as file:
        file.write("\n")
        file.write("=" * 60 + "\n")
        file.write(f"Date & Time : {datetime.now()}\n")
        file.write(f"Feature     : {feature}\n")
        file.write(f"Operation   : {operation}\n")
        file.write(f"Input       : {input_data}\n")
        file.write(f"Output      : {output_data}\n")


# =========================
# File Encryption
# =========================

def encrypt_file(filename, key):

    try:
        with open(filename, "rb") as file:
            data = file.read()

        f = Fernet(key)
        encrypted = f.encrypt(data)

        with open(filename, "wb") as file:
            file.write(encrypted)

        print("\n✅ File Encrypted Successfully!")

    except FileNotFoundError:
        print("\n❌ File not found.")


def decrypt_file(filename, key):

    try:
        with open(filename, "rb") as file:
            data = file.read()

        f = Fernet(key)
        decrypted = f.decrypt(data)

        with open(filename, "wb") as file:
            file.write(decrypted)

        print("\n✅ File Decrypted Successfully!")

    except:
        print("\n❌ Unable to decrypt file.")


# =========================
# Cyber Security Tips
# =========================

tips = [
    "Use strong and unique passwords.",
    "Enable Two-Factor Authentication (2FA).",
    "Never share your encryption key.",
    "Keep your software updated.",
    "Avoid clicking unknown links.",
    "Always back up important data.",
    "Use antivirus software.",
    "Don't reuse passwords on different websites."
]


def show_tip():
    print("\n💡 Cyber Security Tip:")
    print(random.choice(tips))
 # =========================
# Main Menu
# =========================

while True:

    print("\n" + "=" * 60)
    print("      CYBER SECURE ENCRYPTION SUITE")
    print("=" * 60)

    print("1. Caesar Cipher")
    print("2. AES Encryption")
    print("3. Password Strength Checker")
    print("4. File Encryption")
    print("5. File Decryption")
    print("6. View Cyber Security Tip")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ")

    # ---------------- Caesar Cipher ----------------

    if choice == "1":

        print("\n1. Encrypt")
        print("2. Decrypt")

        option = input("Choose option: ")

        text = input("Enter text: ")
        shift = int(input("Enter shift value: "))

        if option == "1":

            encrypted = caesar_encrypt(text, shift)

            print("\nEncrypted Text:", encrypted)

            save_history("Caesar Cipher", "Encryption", text, encrypted)

        elif option == "2":

            decrypted = caesar_decrypt(text, shift)

            print("\nDecrypted Text:", decrypted)

            save_history("Caesar Cipher", "Decryption", text, decrypted)

        else:

            print("Invalid Option")

    # ---------------- AES ----------------

    elif choice == "2":

        key = generate_key()

        text = input("Enter text: ")

        encrypted = aes_encrypt(text, key)

        print("\nGenerated Key:")
        print(key.decode())

        print("\nEncrypted Text:")
        print(encrypted.decode())

        decrypted = aes_decrypt(encrypted, key)

        print("\nDecrypted Text:")
        print(decrypted) 
        
         
                


