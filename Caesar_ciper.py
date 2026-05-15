def encrypt_message(message, shift):
    result = ""
    
    for char in message:
        if char.isalpha():
            char = char.upper()
            position = ord(char) - ord('A')
            new_position = (position + shift) % 26
            new_char = chr(new_position + ord('A'))
            result = result + new_char
        else:
            result = result + char
    
    return result


def decrypt_message(message, shift):
    return encrypt_message(message, -shift)


def main():
    print("=" * 40)
    print("   CAESAR CIPHER - ENCRYPTION TOOL")
    print("=" * 40)
    print()
    
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (number): "))
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()
    
    print()
    
    if choice == 'E':
        encrypted = encrypt_message(message, shift)
        print("Encrypted message:", encrypted)
    elif choice == 'D':
        decrypted = decrypt_message(message, shift)
        print("Decrypted message:", decrypted)
    else:
        print("Invalid choice! Please enter E or D.")


if __name__ == "__main__":
    main()
