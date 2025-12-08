def caesar_encrypt(text: str, shift: int) -> str:
    result = ""
    
    # Normalize shift to avoid large numbers
    shift %= 26

    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += shifted
        else:
            result += char

    return result


def caesar_decrypt(text: str, shift: int) -> str:
    return caesar_encrypt(text, -shift)


if __name__ == "__main__":
    text = "Hello World!"
    shift = 3

    encrypted = caesar_encrypt(text, shift)
    print("Original:", text)
    print("Encrypted:", encrypted)

    decrypted = caesar_decrypt(encrypted, shift)
    print("Decrypted:", decrypted)
