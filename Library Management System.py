class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.read().splitlines()
        for book in books:
            book_info = book.strip().split(',')
            print(f"Title: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_year = input("Enter release year: ")
        pages = input("Enter number of pages: ")
        book_info = f"{title},{author},{release_year},{pages}\n"
        self.file.write(book_info)
        self.file.seek(0)
        print(f"Book'{title}' added successfully.")
    

    def remove_book(self):
        title = input("Enter the title of the book you want to remove: ")
        self.file.seek(0)
        books = self.file.readlines()
        if any(title in book for book in books):
            updated_books = [book for book in books if title not in book]
            self.file.seek(0)
            self.file.truncate()
            self.file.writelines(updated_books)
            print(f"Book '{title}' removed successfully.")
        else:
            print(f"Book '{title}' not found.")




lib = Library()

while True:
    print("*** MENU***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("q) Exit")
    lib.list_books()

    choice = input("Enter your choice: ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice.lower() == 'q':
        print("Logged out successfully")
        break
    else:
        print("Invalid choice")