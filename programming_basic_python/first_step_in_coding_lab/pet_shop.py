nums_of_packeges_dog_food = int(input())
nums_of_packeges_cat_food = int(input())

price_for_packet_dog_food = 2.50 * nums_of_packeges_dog_food
price_for_packet_cat_food = 4 * nums_of_packeges_cat_food
final_price = price_for_packet_dog_food + price_for_packet_cat_food

print(f"{final_price} lv.")