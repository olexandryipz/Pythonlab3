text = input("Введіть текст: ")

words = text.split()
proper_names = [word for word in words if word.istitle()]

print(f"Список імен та власних назв: {proper_names}")