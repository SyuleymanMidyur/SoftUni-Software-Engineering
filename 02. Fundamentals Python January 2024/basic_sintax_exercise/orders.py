number_of_orders = int(input())
total_price = 0
for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsule = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100.00:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsule < 1 or capsule > 2000:
        continue
    price_for_coffe = price_per_capsule * capsule * days
    total_price += price_for_coffe
    print(f"The price for the coffee is: ${price_for_coffe:.2f}")

print(f"Total: ${total_price:.2f}")
