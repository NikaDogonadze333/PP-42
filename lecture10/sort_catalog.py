names = ["Laptop", "Phone", "Headphones", "Monitor"]
prices = [1200, 800, 150, 300]
ratings = [4.8, 4.5, 4.2, 4.9]

products = list(zip(names, prices, ratings))

sorted_by_price = sorted(products, key=lambda x: x[1], reverse=True)
print("Sorted by price (highest to lowest):", sorted_by_price)

sorted_by_rating = sorted(products, key=lambda x: x[2])
print("Sorted by rating (lowest to highest):", sorted_by_rating)