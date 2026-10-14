def even_numbers():
    num = 0
    while True:
        yield num
        num += 2

count = 0
for x in even_numbers():
    print(x)
    count += 1
    if count == 10:
        break