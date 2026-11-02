import requests

BASE_URL = "https://crudcrud.com/api/9b8797f29e8a4a3aa8930e2e93031aca/products"
product_id = "6ae8a0dbcdeb2003e816c4e5"
updated_data = {"name": "Gaming Laptop", "price": 3200, "in_stock": True}

try:
    response = requests.put(f"{BASE_URL}/{product_id}", json=updated_data, timeout=10)
    response.raise_for_status()
    print("სტატუსის კოდი:", response.status_code)
    
    verify_response = requests.get(f"{BASE_URL}/{product_id}", timeout=10)
    verify_response.raise_for_status()
    print(verify_response.json())
except requests.exceptions.RequestException as e:
    print(e)