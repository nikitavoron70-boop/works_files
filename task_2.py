def search_word_in_text():
    try:
        word = input("Введите слово для поиска: ").strip().lower()

        with open('text.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        found_lines = []
        total_count = 0

        for i, line in enumerate(lines, 1):
            line_lower = line.lower()
            count = line_lower.count(word)
            if count > 0:
                found_lines.append(i)
                total_count += count

        print(f"\nРезультаты поиска слова '{word}':")
        if found_lines:
            print(f"Слово найдено")
            print(f"Встречается {total_count} раз(а)")
            print(f"В строках: {', '.join(map(str, found_lines))}")
        else:
            print(f"Слово не найдено")

        with open('search_results.txt', 'w', encoding='utf-8') as file:
            file.write(f"Поиск слова: '{word}'\n")
            file.write(f"{'=' * 40}\n")
            file.write(f"Найдено: {'да' if found_lines else 'нет'}\n")
            file.write(f"Количество вхождений: {total_count}\n")
            if found_lines:
                file.write(f"Строки: {', '.join(map(str, found_lines))}\n")

        print(f"\nРезультаты сохранены в search_results.txt")

    except FileNotFoundError:
        print("Ошибка: файл text.txt не найден")
    except Exception as e:
        print(f"Ошибка: {e}")

search_word_in_text()