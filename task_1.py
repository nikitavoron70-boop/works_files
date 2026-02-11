def count_lines_and_words():
    try:
        with open('input.txt', 'r', encoding='utf-8') as file:
            content = file.readlines()

        lines_count = len(content)
        words_count = sum(len(line.split()) for line in content)

        with open('statistics.txt', 'w', encoding='utf-8') as file:
            file.write(f"Количество строк: {lines_count}\n")
            file.write(f"Количество слов: {words_count}\n")

        print(f"Статистика записана в statistics.txt")

    except FileNotFoundError:
        print("Ошибка: файл input.txt не найден")
    except Exception as e:
        print(f"Ошибка: {e}")

count_lines_and_words()