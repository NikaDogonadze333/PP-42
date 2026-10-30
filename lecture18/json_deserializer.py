from dataclasses import dataclass
import json

@dataclass
class Product:
    name: str
    price: float
    in_stock: bool

raw_json = '{"name": "Laptop", "price": 2500, "in_stock": true}'
parsed_dict = json.loads(raw_json)
restored_product = Product(**parsed_dict)

print(type(restored_product))
print(restored_product.name, restored_product.price, restored_product.in_stock)