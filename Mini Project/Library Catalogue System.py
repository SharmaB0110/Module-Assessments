class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def check_out(self):
        if self.available:
            self.available = False
            print(f'"{self.title}" has been checked out.')
        else:
            print(f'"{self.title}" is already checked out.')

    def return_book(self):
        if not self.available:
            self.available = True
            print(f'"{self.title}" has been returned.')
        else:
            print(f'"{self.title}" is already available.')


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f'Added "{title}" by {author} to the catalogue.')

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def display_books(self):
        if not self.books:
            print("The catalogue is empty.")
            return

        print("\nLibrary catalogue:")
        for book in self.books:
            status = "Available" if book.available else "Checked out"
            print(f'"{book.title}" by {book.author} — {status}')


def main():
    library = Library()

    while True:
        print("\n1. Add a book")
        print("2. Check out a book")
        print("3. Return a book")
        print("4. View catalogue")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Book title: ").strip()
            author = input("Author: ").strip()
            if title and author:
                library.add_book(title, author)
            else:
                print("Title and author cannot be empty.")

        elif choice == "2":
            title = input("Title of the book to check out: ").strip()
            book = library.find_book(title)
            if book:
                book.check_out()
            else:
                print("Book not found.")

        elif choice == "3":
            title = input("Title of the book to return: ").strip()
            book = library.find_book(title)
            if book:
                book.return_book()
            else:
                print("Book not found.")

        elif choice == "4":
            library.display_books()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Please choose a number from 1 to 5.")


main()