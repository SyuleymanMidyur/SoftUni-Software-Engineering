num_of_users = int(input())
usernames = set()
for i in range(num_of_users):
    username = input()
    usernames.add(username)

print(*usernames, sep='\n')
