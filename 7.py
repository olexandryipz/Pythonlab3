text = input("Введіть текст: ")

half_length = len(text) // 2

new_text = text[:half_length].replace("п", "*") + text[half_length:]

print(f"Новий текст: {new_text}")