import requests

BASE_URL = "https://crudcrud.com/api/9b8797f29e8a4a3aa8930e2e93031aca/products"
product_data = {"name": "Laptop", "price": 2500, "in_stock": True}

try:
    response = requests.post(BASE_URL, json=product_data, timeout=10)
    response.raise_for_status()
    print(response.json())
except requests.exceptions.RequestException as e:
    print(e)