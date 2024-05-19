name_of_airline = input()
adults_tickets = int(input())
kids_tickets = int(input())
netto_price_adults = float(input())
taxes = float(input())

netto_price_kids = netto_price_adults * 0.30
price_for_one_ticket_adult = netto_price_adults + taxes
price_for_one_ticket_kid = netto_price_kids + taxes
total_tickets_price = (price_for_one_ticket_adult * adults_tickets) + (price_for_one_ticket_kid * kids_tickets)
profit_of_agency = total_tickets_price * 0.20

print(f"The profit of your agency from {name_of_airline} tickets is {profit_of_agency:.2f} lv.")
