books = []

while True:
    print("\n===== Book Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        books.append(book)
        print("Book added successfully!")

    elif choice == "2":
        if len(books) == 0:
            print("No books available.")
        else:
            print("\nBook List:")
            for b in books:
                print("-", b)

    elif choice == "3":
        search = input("Enter book name to search: ")
        if search in books:
            print("Book found!")
        else:
            print("Book not found.")

    elif choice == "4":
        delete = input("Enter book name to delete: ")
        if delete in books:
            books.remove(delete)
            print("Book deleted successfully!")
        else:
            print("Book not found.")

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice.")