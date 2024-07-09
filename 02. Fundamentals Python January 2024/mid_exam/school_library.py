# shelf_with_books = input().split('&')
# collection_books = [shelf_with_books]
#
# for book in shelf_with_books:
#     command, name = book.split(' | ')
#     if command == 'Add Book':
#         if name in collection_books:
#             continue
#         collection_books.insert(name, 0)
#     elif command == 'Take Book':
#         if name in collection_books:
#             collection_books.remove(name)
#     elif command == 'Swap Book':
#
#     elif command == 'Insert Book':
#         pass
#     elif command == 'Check Book':
#         pass

shelf = input().split("&")

while True:
    command = input().split(" | ")

    if command[0] == "Done":
        break

    action = command[0]
    book_name = command[1]

    if action == "Add Book":
        if book_name not in shelf:
            shelf.insert(0, book_name)
    elif action == "Take Book":
        if book_name in shelf:
            shelf.remove(book_name)
    elif action == "Swap Books":
        book1, book2 = command[1], command[2]
        if book1 in shelf and book2 in shelf:
            index1, index2 = shelf.index(book1), shelf.index(book2)
            shelf[index1], shelf[index2] = shelf[index2], shelf[index1]
    elif action == "Insert Book":
        if book_name not in shelf:
            shelf.append(book_name)
    elif action == "Check Book":
        index = int(book_name)
        if 0 <= index < len(shelf):
            print(shelf[index])

# Output the final collection of books
print(", ".join(shelf))
