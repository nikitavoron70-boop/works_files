def cesar_encrypt(text):
    result = ''
    for char in text:
        if char.isalpha():
            if 'a' <= char <= 'z':
                base = ord('a')
                result += chr((ord(char) - base + 3) % 26 + base)
            elif 'A' <= char <= 'Z':
                base = ord('A')
                result += chr((ord(char) - base + 3) % 26 + base)
            elif 'а' <= char <= 'я':
                base = ord('а')
                result += chr((ord(char) - base + 3) % 33 + base)
            elif 'А' <= char <= 'Я':
                base = ord('А')
                result += chr((ord(char) - base + 3) % 33 + base)
            else:
                result += char
        else:
            result += char
    return result

def cesar_decrypt(text):
    result = ''
    for char in text:
        if char.isalpha():
            if 'a' <= char <= 'z':
                base = ord('a')
                result += chr((ord(char) - base - 3) % 26 + base)
            elif 'A' <= char <= 'Z':
                base = ord('A')
                result += chr((ord(char) - base - 3) % 26 + base)
            elif 'а' <= char <= 'я':
                base = ord('а')
                result += chr((ord(char) - base - 3) % 33 + base)
            elif 'А' <= char <= 'Я':
                base = ord('А')
                result += chr((ord(char) - base - 3) % 33 + base)
            else:
                result += char
        else:
            result += char
    return result

with open('resource/secret.txt', 'r', encoding='utf-8') as file:
    original_text = file.read()

encrypted_text = cesar_encrypt(original_text)

with open('resource/encrypted.txt', 'w', encoding='utf-8') as file:
    file.write(encrypted_text)

with open('resource/encrypted.txt', 'r', encoding='utf-8') as file:
    encrypted_content = file.read()

decrypted_text = cesar_decrypt(encrypted_content)

with open('resource/decrypted.txt', 'w', encoding='utf-8') as file:
    file.write(decrypted_text)