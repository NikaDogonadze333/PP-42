from dataclasses import dataclass, asdict
import json

@dataclass
class Product:
    name: str
    price: float
    in_stock: bool

p1 = Product("Laptop", 2500.0, True)
p2 = Product("Mouse", 80.0, True)
p3 = Product("Keyboard", 150.0, False)

products_list = [asdict(p1), asdict(p2), asdict(p3)]
json_data = json.dumps(products_list, indent=4)
print(json_data)