cart_total = 60.0
is_vip = False
is_guest = False
promo_code = "SAVE10"

# Free shipping check
if cart_total >= 50 or is_vip:
    print("You get Free Shipping!")
else:
    print("You need to pay for shipping.")

# Discount check
if promo_code and not is_guest:
    cart_total = cart_total * 0.9
    print(f"10% discount applied! Total price: ${cart_total}")
else:
    print(f"No discount applied. Total price: ${cart_total}")