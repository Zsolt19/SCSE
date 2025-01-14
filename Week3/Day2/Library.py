class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True  # Book is available by default

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return True
        return False  # If book is already borrowed, return False

    def return_book(self):
        self.is_available = True

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Available: {'Yes' if self.is_available else 'No'}"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is currently unavailable.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} didn't borrow '{book.title}'.")

    def __str__(self):
        borrowed_books_titles = [book.title for book in self.borrowed_books]
        return f"Name: {self.name}, ID: {self.member_id}, Borrowed Books: {', '.join(borrowed_books_titles) if borrowed_books_titles else 'None'}"


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: '{book.title}' by {book.author}.")

    def add_member(self, member):
        self.members.append(member)
        print(f"Added member: {member.name} (ID: {member.member_id}).")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(book)

    def list_members(self):
        if not self.members:
            print("No members in the library.")
        else:
            print("Library members:")
            for member in self.members:
                print(member)

# Demonstrating the system
def main():
    # Create books
    book1 = Book("To Kill a Mockingbird", "Harper Lee")
    book2 = Book("1984", "George Orwell")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

    # Create members
    member1 = Member("Alice", 101)
    member2 = Member("Bob", 102)

    # Create library
    library = Library()

    # Add books and members to the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_member(member1)
    library.add_member(member2)

    # List all books and members
    library.list_books()
    library.list_members()

    # Members borrow and return books
    member1.borrow_book(book1)  # Alice borrows book1
    member2.borrow_book(book2)  # Bob borrows book2
    member1.borrow_book(book2)  # Alice tries to borrow book2, but it's unavailable
    member1.return_book(book1)  # Alice returns book1
    member2.return_book(book2)  # Bob returns book2

    # Final list of books and members
    library.list_books()
    library.list_members()

if __name__ == "__main__":
    main()
