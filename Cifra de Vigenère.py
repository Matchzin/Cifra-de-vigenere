def encrypt_vigenere(plain_text, key):
    encrypted_text = ""
    key = key.upper()
    key_idx = 0

    for char in plain_text:
        if char.isalpha():
            shift = ord(key[key_idx]) - ord('A')
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted_text += encrypted_char

            key_idx = (key_idx + 1) % len(key)
        else:
            encrypted_text += char

    return encrypted_text


def decrypt_vigenere(encrypted_text, key):
    decrypted_text = ""
    key = key.upper()
    key_idx = 0

    for char in encrypted_text:
        if char.isalpha():
            shift = ord(key[key_idx]) - ord('A')
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            decrypted_text += decrypted_char

            key_idx = (key_idx + 1) % len(key)
        else:
            decrypted_text += char

    return decrypted_text


def main():
    option = input("Digite 'E' para criptografar ou 'D' para descriptografar: ")
    text = input("Digite o texto: ")
    key = input("Digite a chave: ")

    if option.upper() == 'E':
        encrypted_text = encrypt_vigenere(text, key)
        print("Texto criptografado:", encrypted_text)
    elif option.upper() == 'D':
        decrypted_text = decrypt_vigenere(text, key)
        print("Texto descriptografado:", decrypted_text)
    else:
        print("Opção inválida. Digite 'E' ou 'D'.")


if __name__ == "__main__":
    main()
