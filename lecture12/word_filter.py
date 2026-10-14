words = ["python", "generator", "yield", "code", "ai", "developer"]

long_words = (w.upper() for w in words if len(w) > 4)

for word in long_words:
    print(word)