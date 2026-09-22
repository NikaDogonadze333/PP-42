correct_pin = 1234
balance = 500.0
requested_amount = 100.0

user_pin = int(input("Enter your PIN: "))

if user_pin == correct_pin:
    if requested_amount <= balance:
        balance = balance - requested_amount
        print(f"Withdrawal successful! Remaining balance: ${balance}")
    else:
        print("Amount of your balance isn't enough.")
else:
    print("Incorrect PIN. Access Denied.")