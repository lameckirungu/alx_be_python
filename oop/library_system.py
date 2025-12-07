class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    # Helper method for consistent output for the base class
    def get_details(self) -> str:
        return f"Book: {self.title} by {self.author}"
    

class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

    # Polymorphism: Ovverrides the base method to add file_size
    def get_details(self) -> str:
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"
    

class PrintBook(Book):
    
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def get_details(self) -> str:
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library: 
    def __init__(self):
        self.books = []
 
    def add_book(self, book : Book):
        # Checks if the object is an instance of Book or any derived class
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print(f"Error: {book} is not a valid book type.", file=sys.stderr)

    def list_books(self):
        for book in self.books:
            print(book.get_details())

