followers = {}

while True:
    command = input()
    if command == "Log out":
        break

    tokens = command.split(": ")
    action = tokens[0]
    username = tokens[1]

    if action == "New follower":
        if username not in followers:
            followers[username] = {"likes": 0, "comments": 0}
    elif action == "Like":
        count = int(tokens[2])
        if username not in followers:
            followers[username] = {"likes": count, "comments": 0}
        else:
            followers[username]["likes"] += count
    elif action == "Comment":
        if username not in followers:
            followers[username] = {"likes": 0, "comments": 1}
        else:
            followers[username]["comments"] += 1
    elif action == "Blocked":
        if username in followers:
            del followers[username]
        else:
            print(f"{username} doesn't exist.")

# followers_sorted = dict(sorted(followers.items(), key=lambda x: (-x[1]["likes"], x[0])))

print(f"{len(followers)} followers")
for username, info in followers.items():
    print(f"{username}: {info['likes'] + info['comments']}")
