num_lines = 0
num_words = 0

with open('resource/input.txt', 'r', encoding='utf-8') as infile:
    for line in infile:
        num_lines += 1
        words_in_line = line.split()
        num_words += len(words_in_line)

with open('resource/statistics.txt', 'w', encoding='utf-8') as outfile:
    outfile.write(f'Количество строк: {num_lines}\n')
    outfile.write(f'Количество слов: {num_words}\n')