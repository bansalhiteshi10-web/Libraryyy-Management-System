# LIBRARY MANAGEMENT SYSTEM
# Basic Python Project

books = []


# Add a new book
def add_book():
    print("\n--- Add Book ---")

    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    # Check if Book ID already exists
    for book in books:
        if book["id"] == book_id:
            print("Book ID already exists.")
            return

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "status": "Available",
        "issued_to": ""
    }

    books.append(book)
    print("Book added successfully.")


# Display all books
def display_books():
    print("\n--- All Books ---")

    if len(books) == 0:
        print("No books available in the library.")
        return

    for book in books:
        print("-----------------------------")
        print("Book ID     :", book["id"])
        print("Title       :", book["title"])
        print("Author      :", book["author"])
        print("Status      :", book["status"])

        if book["status"] == "Issued":
            print("Issued To   :", book["issued_to"])

    print("-----------------------------")


# Search for a book
def search_book():
    print("\n--- Search Book ---")

    book_id = input("Enter Book ID to search: ")

    for book in books:
        if book["id"] == book_id:
            print("\nBook Found")
            print("Book ID     :", book["id"])
            print("Title       :", book["title"])
            print("Author      :", book["author"])
            print("Status      :", book["status"])

            if book["status"] == "Issued":
                print("Issued To   :", book["issued_to"])

            return

    print("Book not found.")


# Issue a book
def issue_book():
    print("\n--- Issue Book ---")

    book_id = input("Enter Book ID: ")
    student_name = input("Enter Student Name: ")

    for book in books:
        if book["id"] == book_id:

            if book["status"] == "Issued":
                print("This book is already issued.")
                return

            book["status"] = "Issued"
            book["issued_to"] = student_name

            print("Book issued successfully to", student_name)
            return

    print("Book not found.")


# Return a book
def return_book():
    print("\n--- Return Book ---")

    book_id = input("Enter Book ID: ")

    for book in books:
        if book["id"] == book_id:

            if book["status"] == "Available":
                print("This book is already available in the library.")
                return

            book["status"] = "Available"
            book["issued_to"] = ""

            print("Book returned successfully.")
            return

    print("Book not found.")


# Remove a book
def remove_book():
    print("\n--- Remove Book ---")

    book_id = input("Enter Book ID: ")

    for book in books:
        if book["id"] == book_id:

            if book["status"] == "Issued":
                print("Cannot remove an issued book.")
                return

            books.remove(book)
            print("Book removed successfully.")
            return

    print("Book not found.")


# Main menu
def main():
    while True:

        print("\n===================================")
        print("      LIBRARY MANAGEMENT SYSTEM")
        print("===================================")
        print("1. Add Book")
        print("2. Display All Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Remove Book")
        print("7. Exit")
        print("===================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            display_books()

        elif choice == "3":
            search_book()

        elif choice == "4":
            issue_book()

        elif choice == "5":
            return_book()

        elif choice == "6":
            remove_book()

        elif choice == "7":
            print("Thank you for using Library Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
main()