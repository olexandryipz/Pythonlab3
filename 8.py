text = input("Введіть текст: ")

word = input("Введіть слово: ").lower()

count = text.lower().split().count(word)

print(f"Кількість входжень слова '{word}': {count}")
