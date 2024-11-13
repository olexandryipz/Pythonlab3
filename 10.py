text = input("Введіть текст: ")

n = input("Введіть літеру N: ").lower()
p = input("Введіть літеру P: ").lower()

words = text.split()
matching_words = [word for word in words if word.lower().startswith(n) or word.lower().endswith(p)]

print(f"Слова, що починаються на '{n}' або закінчуються на '{p}': {', '.join(matching_words)}")
