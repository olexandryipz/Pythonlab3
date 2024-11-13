text = input("Введіть текст: ")

new_text = text.replace("о", "")
removed_count = text.count("о")

print(f"Новий текст: {new_text}")
print(f"Кількість видалених літер 'о': {removed_count}")