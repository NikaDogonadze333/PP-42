class Payment:
    def process_payment(self, amount):
        print(f"მიმდინარეობს გადახდა... {amount} ლარი")

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"საბანკო ბარათით გადახდილია: {amount} ლარი")

class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"PayPal-ით გადახდილია: {amount} ლარი")