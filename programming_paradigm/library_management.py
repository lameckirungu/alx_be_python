class Book:
    """
    Represents a book in the library.

    Attributes:
        title (str): The title of the book (public).
        author (str): The author of the book (public).
        _is_checked_out (bool): Indicates if the book is checked out (private).
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def add_book(self, book):
        self._books.append(book)

    def check_out(self):
        """Marks the book as checked out."""
        self._is_checked_out = True

    def is_available(self):
        """Returns True if the book is available, False otherwise."""
        return not self._is_checked_out
    def return_book(self):
        """Marks the book as returned."""
        self._is_checked_out = False
        

class Library:
    """Manages a collection of Book objects."""
    def __init__(self):
        self._books = []
    
    def add_book(self, book):
        """Adds a book to the library's collection."""
        self._books.append(book)
        print(f"Added '{book.title}' by {book.author}.")
    
    def check_out_book(self, title):
        """Finds a book by title and marks it as checked out if available."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.check_out()
                return True
        print(f"Error: '{title}' not found or already checked out.")
        return False
    
    def return_book(self, title):
        """Finds a book by title and marks it as returned."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        print(f"Error: Cannot return '{title}'. It was not checked out.")
        return False

    def list_available_books(self):
        """Prints the title and author of all available books."""

        for book in self._books:
            if book.is_available():                
                print(f"'{book.title}' by {book.author} is available.")
                return True
            print(f"'{book.title}' by {book.author} is not available for borrowing.")
            return False