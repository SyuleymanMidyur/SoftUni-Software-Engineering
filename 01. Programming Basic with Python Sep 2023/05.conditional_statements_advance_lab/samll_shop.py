type_of_product = input()
city = input()
quantity = float(input())
price = 0

if city == "Sofia":
    if type_of_product == "coffee":
        price = quantity * 0.50
    elif type_of_product == "water":
        price = quantity * 0.80
    elif type_of_product == "beer":
        price = quantity * 1.20
    elif type_of_product == "sweets":
        price = quantity * 1.45
    elif type_of_product == "peanuts":
        price = quantity * 1.60
elif city == "Plovdiv":
    if type_of_product == "coffee":
        price = quantity * 0.40
    elif type_of_product == "water":
        price = quantity * 0.70
    elif type_of_product == "beer":
        price = quantity * 1.15
    elif type_of_product == "sweets":
        price = quantity * 1.30
    elif type_of_product == "peanuts":
        price = quantity * 1.50

elif city == "Varna":
    if type_of_product == "coffee":
        price = quantity * 0.45
    elif type_of_product == "water":
        price = quantity * 0.70
    elif type_of_product == "beer":
        price = quantity * 1.10
    elif type_of_product == "sweets":
        price = quantity * 1.35
    elif type_of_product == "peanuts":
        price = quantity * 1.55

print(price)