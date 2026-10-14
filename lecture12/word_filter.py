words = ["python", "generator", "yield", "code", "ai", "developer"]

long_words = (word.upper() for word in words if len(word) > 4)

for item in long_words:
    print(item)
