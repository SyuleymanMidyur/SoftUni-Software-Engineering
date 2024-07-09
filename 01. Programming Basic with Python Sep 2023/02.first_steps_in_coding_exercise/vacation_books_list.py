nums_of_pages = int(input())
pages_per_hour = int(input())
nums_of_days = int(input())

total_time_to_read_book = nums_of_pages / pages_per_hour
time_per_day_for_read = total_time_to_read_book / nums_of_days

print(int(time_per_day_for_read))