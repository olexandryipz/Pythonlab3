text = input("Введіть текст: ")

new_text = text.replace("а", "о")
replacements = text.count("а")

print(f"Новий текст: {new_text}")
print(f"Кількість замін: {replacements}")
print(f"Загальна кількість символів у рядку: {len(new_text)}")