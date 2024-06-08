num_of_guests = int(input())

reservations = set()

for _ in range(num_of_guests):
    reservation_code = input()
    reservations.add(reservation_code)

while True:
    guest_code = input()
    if guest_code == "END":
        break
    if guest_code in reservations:
        reservations.remove(guest_code)

print(len(reservations))
for reservation in sorted(reservations):
    print(reservation)
