text = input("Введіть текст (до 1000 слів): ")

letter = input("Введіть літеру: ").lower()

words = text.split()

count = sum(1 for word in words if word.lower().startswith(letter))

print(f"Кількість слів, що починаються з літери '{letter}': {count}")