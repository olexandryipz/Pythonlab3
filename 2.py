text = input("Введіть текст: ")

new_text = text.replace(":", "%")
replacements = text.count(":")

print(f"Новий текст: {new_text}")
print(f"Кількість замін: {replacements}")