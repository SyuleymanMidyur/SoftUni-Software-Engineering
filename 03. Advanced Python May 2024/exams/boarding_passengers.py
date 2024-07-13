def boarding_passengers(ship_capacity, *passenger_groups):
    boarded_guests = {}
    available_capacity = ship_capacity

    for group in passenger_groups:
        num_passengers, benefits_program = group
        if num_passengers <= available_capacity:
            if benefits_program not in boarded_guests:
                boarded_guests[benefits_program] = 0
            boarded_guests[benefits_program] += num_passengers
            available_capacity -= num_passengers

    sorted_boarding_details = sorted(boarded_guests.items(), key=lambda x: (-x[1], x[0]))

    result = "Boarding details by benefit plan:\n"
    for benefits_program, total_guests in sorted_boarding_details:
        result += f"## {benefits_program}: {total_guests} guests\n"

    if available_capacity == 0 and sum(boarded_guests.values()) == sum([group[0] for group in passenger_groups]):
        result += "All passengers are successfully boarded!"
    elif available_capacity == 0:
        result += "Boarding unsuccessful. Cruise ship at full capacity."
    else:
        result += f"Partial boarding completed. Available capacity: {available_capacity}."

    return result


# Example usage:
print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))
