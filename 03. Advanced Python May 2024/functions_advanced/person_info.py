def get_info(name, age, town):
    return f"The is {name} from {town} and he is {age} years old"


print(get_info(**{"name": "Tefik", "town": "Debren", "age": "20"}))

