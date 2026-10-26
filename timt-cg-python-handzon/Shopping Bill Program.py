products = {
    "Keyboard": 500,
    "Mouse": 300,
    "Headphone": 700,
    "USB Cable": 200,
    "Speaker": 400
}


def calculate_total(products):
    return sum(products.values())


print("----- Shopping Bill -----")

for product, price in products.items():
    print(product, ":", price)

total = calculate_total(products)

if total >= 1000:
    discount = total * 10 / 100
else:
    discount = 0

final_bill = total - discount

print("\nTotal Price:", total)
print("Discount:", discount)
print("Final Bill Amount:", final_bill)