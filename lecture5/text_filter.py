text = input("Enter text: ")
filtered_text = ""

for char in text:
    if char.isdigit():
        continue
    filtered_text += char

print(filtered_text)