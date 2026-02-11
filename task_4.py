def caesar(text, shift):
    result = ""
    for char in text:
        if 'а' <= char <= 'я':
            result += chr((ord(char) - ord('а') + shift) % 32 + ord('а'))
        elif 'А' <= char <= 'Я':
            result += chr((ord(char) - ord('А') + shift) % 32 + ord('А'))
        elif 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
    return result


try:
    with open('secret.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    with open('encrypted.txt', 'w', encoding='utf-8') as f:
        f.write(caesar(text, 3))

    print("Зашифровано: encrypted.txt")

except:
    print("Ошибка чтения secret.txt")

try:
    with open('encrypted.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    with open('decrypted.txt', 'w', encoding='utf-8') as f:
        f.write(caesar(text, -3))

    print("Расшифровано: decrypted.txt")

except:
    print("Ошибка чтения encrypted.txt")