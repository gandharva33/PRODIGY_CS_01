def caesar_cipher(message, shift):
    result = ""

    for char in message:
        if char.isalpha():
            base = ord('A')
            new_char = chr((ord(char.upper()) - base + shift) % 26 + base)
            result += new_char
        else:
            result += char

    return result


def main():
    print("=" * 40)
    print("   CAESAR CIPHER - ENCRYPTION TOOL")
    print("=" * 40)

    message = input("Enter your message : ")
    shift   = int(input("Enter shift number  : "))
    choice  = input("Encrypt or Decrypt? (E/D) : ").upper()

    if choice == 'E':
        output = caesar_cipher(message, shift)
        print("\nEncrypted Message :", output)

    elif choice == 'D':
        output = caesar_cipher(message, -shift)
        print("\nDecrypted Message :", output)

    else:
        print("Invalid choice! Please enter E or D.")


if __name__ == "__main__":
    main()
