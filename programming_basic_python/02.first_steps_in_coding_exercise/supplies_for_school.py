nums_of_pens_packets = int(input())
nums_of_markers_packets = int(input())
liter_of_cl_detergens = int(input())
discount_procent = int(input())

price_of_pens_packets = nums_of_pens_packets * 5.80
price_of_marker_packets = nums_of_markers_packets * 7.20
total_price_for_detergens = liter_of_cl_detergens * 1.20
price_for_all_materials = price_of_pens_packets + price_of_marker_packets + total_price_for_detergens
total_amount_any_needed = price_for_all_materials - (price_for_all_materials * discount_procent / 100)

print(total_amount_any_needed)