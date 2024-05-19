annual_fee_per_year = int(input())

basketball_shoes = annual_fee_per_year - (annual_fee_per_year * 40) / 100
basketball_uniform = basketball_shoes - (basketball_shoes * 20) / 100
basket_ball = basketball_uniform / 4
basketball_accessories = basket_ball / 5
basketball_equipment = basketball_shoes + basketball_uniform + basket_ball + basketball_accessories
total_cost = annual_fee_per_year + basketball_equipment

print(total_cost)