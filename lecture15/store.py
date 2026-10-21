class Product:
    shop_name = "MegaShop"

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            print(f"მაღაზია: {Product.shop_name} — გაიყიდა {quantity} ცალი {self.name}, დარჩა: {self.stock}")
        else:
            print(f"ბოდიში, {self.name}-ს მარაგში საკმარისი რაოდენობა არ არის!")

laptop = Product("ლეპტოპი", 2500, 10)
laptop.sell(2)