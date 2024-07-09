# number_of_commands = int(input())
#
# register_dict = {}
#
# for _ in range(number_of_commands):
#     command = input()
#
#     action, user, license_platte_number = command.split()
#
#     if user not in register_dict:
#         register_dict[user] = license_platte_number
#         print(f'{user} registered {license_platte_number} successfully')
#     else:
#         print(f'ERRORL already registered with platte number {license_platte_number}')
#
# print(register_dict)

def register_user(username, license_plate, database):
    if username in database:
        print(f"ERROR: already registered with plate number {database[username]}")
    else:
        database[username] = license_plate
        print(f"{username} registered {license_plate} successfully")


def unregister_user(username, database):
    if username not in database:
        print(f"ERROR: user {username} not found")
    else:
        del database[username]
        print(f"{username} unregistered successfully")


def print_registered_users(database):
    for username, license_plate in database.items():
        print(f"{username} => {license_plate}")


number_of_commands = int(input())
parking_database = {}

for _ in range(number_of_commands):
    command = input().split()
    action = command[0]
    if action == "register":
        username, license_plate = command[1], command[2]
        register_user(username, license_plate, parking_database)
    elif action == "unregister":
        username = command[1]
        unregister_user(username, parking_database)

print_registered_users(parking_database)
