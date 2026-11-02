import requests

BASE_URL = "https://crudcrud.com/api/9b8797f29e8a4a3aa8930e2e93031aca/products"
product_id = "6ae8a0dbcdeb2003e816c4e5"

try:
    response = requests.delete(f"{BASE_URL}/{product_id}", timeout=10)
    response.raise_for_status()
    print("სტატუსის კოდი:", response.status_code)
    print("პროდუქტი წარმატებით წაიშალა სერვერიდან")
except requests.exceptions.RequestException as e:
    print(e)