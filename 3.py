text = input("Введіть текст: ")

new_text = text.replace(".", "")
removed_count = text.count(".")

print(f"Новий текст: {new_text}")
print(f"Кількість видалених крапок: {removed_count}")