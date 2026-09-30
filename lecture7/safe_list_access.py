fruits = ["apple", "banana", "cherry", "orange"]

try:
    index = int(input("Enter an index number: "))
    print(f"Selected fruit: {fruits[index]}")
except ValueError:
    print("Invalid input! Please enter a whole number.")
except IndexError:
    max_index = len(fruits) - 1
    print(f"Index out of bounds! Choose an index between 0 and {max_index}.")
else:
    print("Successfully retrieved item!")