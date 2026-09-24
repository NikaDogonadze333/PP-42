n = int(input("Enter a positive integer: "))
even_sum = 0

for i in range(2, n + 1, 2):
    even_sum += i

print(f"The sum of even numbers from 1 to {n} is: {even_sum}")