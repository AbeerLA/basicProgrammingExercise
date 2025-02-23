class Book:
    def __init__(self, title, author, ISBN, available=True):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available = available

    def borrow_book(self):
        """Mark the book as borrowed (unavailable)"""
        if self.available:
            self.available = False
            print(f'You have borrowed "{self.title}" by {self.author}.')
        else:
            print(f'Sorry, "{self.title}" is currently unavailable.')

    def return_book(self):
        """Mark the book as returned (available)"""
        if not self.available:
            self.available = True
            print(f'You have returned "{self.title}".')
        else:
            print(f'"{self.title}" was not borrowed.')

    def show_info(self):
        """Display book details"""
        status = "Available" if self.available else "Borrowed"
        return f'Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}, Status: {status}'


# List to store books
books = []

while True:
    print("\n-- Library Menu --")
    print("1. List Books")
    print("2. Add Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    menu = input("Select menu: ")

    if menu == "1":
        if not books:
            print("No books in the library.")
        else:
            for index, book in enumerate(books):
                print(f"{index}: {book.show_info()}")

    elif menu == "2":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        ISBN = input("Enter book ISBN: ")
        books.append(Book(title, author, ISBN))
        print(f'Book "{title}" added to the library.')

    elif menu == "3":
        if not books:
            print("No books available to borrow.")
        else:
            index = int(input("Choose book index: "))
            if 0 <= index < len(books):
                books[index].borrow_book()
            else:
                print("Invalid book index.")

    elif menu == "4":
        if not books:
            print("No books in the library.")
        else:
            index = int(input("Choose book index: "))
            if 0 <= index < len(books):
                books[index].return_book()
            else:
                print("Invalid book index.")

    elif menu == "5":
        print("Exiting Library System. Goodbye!")
        break

    else:
        print("Invalid selection. Please choose a valid option.")
