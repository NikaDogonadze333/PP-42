from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    in_stock: bool

p1 = Product("Laptop", 2500.0, True)
p2 = Product("Mouse", 80.0, True)
p3 = Product("Keyboard", 150.0, False)

print(p1)
print(p2)
print(p3)