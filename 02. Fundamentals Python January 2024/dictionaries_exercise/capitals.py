countries = input().split(', ')
cities = input().split(', ')

capitals = dict(zip(countries, cities))

for country, city in capitals.items():
    print(f'{country} -> {city}')
