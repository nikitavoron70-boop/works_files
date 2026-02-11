def sort_words():
    try:
        with open('words.txt', 'r', encoding='utf-8') as file:
            words = [line.strip() for line in file if line.strip()]

        if not words:
            print("Файл words.txt пуст")
            return

        print(f"Загружено слов: {len(words)}")
        print(f"Первые 5 слов: {words[:5]}\n")

        sorted_alpha = sorted(words)
        with open('sorted_alphabetically.txt', 'w', encoding='utf-8') as file:
            file.write("=== СОРТИРОВКА ПО АЛФАВИТУ (A-Z) ===\n\n")
            file.write('\n'.join(sorted_alpha))
        print("✓ sorted_alphabetically.txt создан")

        sorted_by_length = sorted(words, key=lambda x: (len(x), x))
        with open('sorted_by_length.txt', 'w', encoding='utf-8') as file:
            file.write("=== СОРТИРОВКА ПО ДЛИНЕ СЛОВА ===\n\n")
            for word in sorted_by_length:
                file.write(f"{word} ({len(word)})\n")
        print("✓ sorted_by_length.txt создан")

        sorted_reverse = sorted(words, reverse=True)
        with open('sorted_reverse.txt', 'w', encoding='utf-8') as file:
            file.write("=== СОРТИРОВКА ПО АЛФАВИТУ (Z-A) ===\n\n")
            file.write('\n'.join(sorted_reverse))
        print("✓ sorted_reverse.txt создан")

        print(f"\nСтатистика:")
        print(f"Самое короткое слово: {min(words, key=len)} ({len(min(words, key=len))} букв)")
        print(f"Самое длинное слово: {max(words, key=len)} ({len(max(words, key=len))} букв)")

    except FileNotFoundError:
        print("Ошибка: файл words.txt не найден")
    except Exception as e:
        print(f"Ошибка: {e}")

sort_words()