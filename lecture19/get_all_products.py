import requests

BASE_URL = "https://crudcrud.com/api/9b8797f29e8a4a3aa8930e2e93031aca/products"

try:
    response = requests.get(BASE_URL, timeout=10)
    response.raise_for_status()
    products = response.json()
    for product in products:
        print(f"სახელი: {product.get('name')}, ფასი: {product.get('price')}, ID: {product.get('_id')}")
except requests.exceptions.RequestException as e:
    print(e)