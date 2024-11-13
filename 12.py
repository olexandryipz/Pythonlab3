text = input("Введіть текст: ")

consonants = "bcdfghjklmnpqrstvwxyz"

count = sum(1 for char in text.lower() if char in consonants)

print(f"Кількість приголосних літер: {count}")
