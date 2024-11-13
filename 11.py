text = input("Введіть текст: ")

vowels = "aeiou"

count = sum(1 for char in text.lower() if char in vowels)

print(f"Кількість голосних літер: {count}")
