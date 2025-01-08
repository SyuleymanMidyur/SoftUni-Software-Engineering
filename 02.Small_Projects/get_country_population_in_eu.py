import requests
from bs4 import BeautifulSoup
import json
import os
import re


def fetch_and_parse_data():
    url = 'https://en.wikipedia.org/wiki/List_of_European_Union_member_states_by_population'
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return {}

    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'class': 'wikitable'})

    if not table:
        print("Failed to find the population table on the page.")
        return {}

    rows = table.find_all('tr')[1:]
    countries_dictionary = {}

    for row in rows:
        columns = row.find_all('td')
        if len(columns) >= 3:
            country = columns[0].text.strip()

            population_str = re.sub(r'[^\d]', '', columns[1].text.strip())

            population = int(population_str)

            countries_dictionary[country] = {'country_population': population}

    return countries_dictionary


def calculate_percentages(countries_dictionary):
    total_population = sum(country['country_population'] for country in countries_dictionary.values())

    if total_population == 0:
        print("Total population is zero. Cannot calculate percentages.")
        return countries_dictionary

    for country in countries_dictionary:
        population = countries_dictionary[country]['country_population']
        percentage = (population / total_population) * 100
        countries_dictionary[country]['country_population_percentage'] = round(percentage, 1)

    return countries_dictionary


def save_to_file(data, filename='eu_population_data.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def load_from_file(filename='eu_population_data.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return None


def main():
    new_data = fetch_and_parse_data()

    if not new_data:
        print("No data fetched. Exiting.")
        return

    new_data = calculate_percentages(new_data)

    existing_data = load_from_file()

    if existing_data != new_data:
        save_to_file(new_data)
        print("New data saved to file.")
    else:
        print("No changes in data. File not updated.")

    print(json.dumps(new_data, indent=4))


if __name__ == "__main__":
    main()
