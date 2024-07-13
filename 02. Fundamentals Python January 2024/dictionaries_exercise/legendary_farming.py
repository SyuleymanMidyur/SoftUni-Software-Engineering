def obtain_legendary(materials):
    legendary_items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
    for material, quantity in materials.items():
        if material in legendary_items and quantity >= 250:
            legendary_item = legendary_items[material]
            print(f"{legendary_item.capitalize()} obtained!")
            materials[material] -= 250
            return True, legendary_item
    return False, None


key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk_items = {}

while True:
    line = input().split()
    for i in range(0, len(line), 2):
        quantity = int(line[i])
        material = line[i + 1].lower()
        if material in key_materials:
            key_materials[material] += quantity
            obtained, legendary_item = obtain_legendary(key_materials)
            if obtained:
                break
        else:
            if material not in junk_items:
                junk_items[material] = 0
            junk_items[material] += quantity
    else:
        continue
    break

for material, quantity in key_materials.items():
    print(f"{material}: {quantity}")

for material, quantity in junk_items.items():
    print(f"{material}: {quantity}")
