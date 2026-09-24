correct_pin = "1234"
attempts = 3

while attempts > 0:
    user_pin = input("Enter PIN: ")
    
    if user_pin == correct_pin:
        print("Access granted!")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Incorrect PIN. Remaining attempts: {attempts}")
        else:
            print("Card blocked!")