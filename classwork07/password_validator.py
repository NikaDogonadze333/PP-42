try:
    password = input("Enter a password: ")
    if len(password) < 6:
        raise ValueError("Password is too short!")
    print("Password accepted!")
except ValueError as e:
    print(e)