with open('resource/words.txt', 'r', encoding='utf-8') as file:
    words = [line.strip() for line in file]

sorted_alphabetically = sorted(words, key=lambda x: x.lower())
with open('resource/sorted_alphabetically.txt', 'w', encoding='utf-8') as file:
    for word in sorted_alphabetically:
        file.write(word + '\n')

sorted_by_length = sorted(words, key=len)
with open('resource/sorted_by_length.txt', 'w', encoding='utf-8') as file:
    for word in sorted_by_length:
        file.write(word + '\n')

sorted_reverse = sorted(words, key=lambda x: x.lower(), reverse=True)
with open('resource/sorted_reverse.txt', 'w', encoding='utf-8') as file:
    for word in sorted_reverse:
        file.write(word + '\n')