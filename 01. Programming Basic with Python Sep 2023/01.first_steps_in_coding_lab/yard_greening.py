square_meters_for_landscaping = float(input())
price_without_discount = square_meters_for_landscaping * 7.61
discount_price = 0.18 * price_without_discount
final_price = price_without_discount - discount_price


print(f"The final price is: {final_price} lv.")

print(f"The discount is: {discount_price} lv.")