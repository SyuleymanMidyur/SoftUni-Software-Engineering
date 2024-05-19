movie_name = input()

total_tickets = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while movie_name != "Finish":
    free_seats = int(input())
    sold_ticket = 0

    for ticket in range(free_seats):
        kind_of_ticket = input()
        if kind_of_ticket == "End":
            break
        elif kind_of_ticket == "student":
            student_tickets += 1
        elif kind_of_ticket == "standard":
            standard_tickets += 1
        elif kind_of_ticket == "kid":
            kid_tickets += 1
        sold_ticket += 1

    percentage_full_seats = (sold_ticket / free_seats) * 100
    print(f"{movie_name} - {percentage_full_seats:.2f}% full.")
    movie_name = input()

total_sold_tickets = student_tickets + standard_tickets + kid_tickets
percentage_student_tickets = (student_tickets / total_sold_tickets) * 100
percentage_standard_tickets = (standard_tickets / total_sold_tickets) * 100
percentage_kid_tickets = (kid_tickets / total_sold_tickets) * 100

print(f"Total tickets: {total_sold_tickets}")
print(f"{percentage_student_tickets:.2f}% student tickets.")
print(f"{percentage_standard_tickets:.2f}% standard tickets.")
print(f"{percentage_kid_tickets:.2f}% kids tickets.")
