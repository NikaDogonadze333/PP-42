def even_numbers():
    num = 0
    while True:
        yield num
        num += 2

count = 0
for item in even_numbers():
    print(item)
    count += 1
    if count == 10:
        break
