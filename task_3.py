files = ['file1.txt', 'file2.txt', 'file3.txt']

with open('combined.txt', 'w', encoding='utf-8') as result:
    for filename in files:
        try:
            result.write(f'=== Содержимое {filename} ===\n')

            with open(filename, 'r', encoding='utf-8') as f:
                result.write(f.read())

            result.write('\n\n')

            print(f'Файл {filename} добавлен')

        except FileNotFoundError:
            result.write('[ФАЙЛ НЕ НАЙДЕН]\n\n')
            print(f'Файл {filename} не найден')

print('Готово! Файл combined.txt создан')