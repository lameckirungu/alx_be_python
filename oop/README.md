# Concept: OOP
- This project dives deeper into the world of OOP in Python.
- It explores advanced concepts like constructors, destructors, magic methods, inheritance, composition, polymorphism, and more.

# Project Objectives
 - Describe the functionalities of constructors (`__init__`), desctructors (`__del__`), and common magic methods (`__str__`, `__repr__`) in Python classes.
 - Implement inheritance to create new classes that inherit properties and methods from existing classes.
 - Utilizing composition as an alternative to inheritance for building complex objects.
 - Explain the concepts of single, multiple, and multilevel inheritance in Python.
 - Understand the method resolution order (MRO) in Python and how it affects method calls in inheritance hierarchies.
 - Implement polymorphism and method overriding to create flexible and reusable code.
 - Explain and use Python's duck typing to achieve polymorphic behavior.
 - Distinguish between class methods and static methods based on their usage and purpose.
 - Apply `@classmethod` and `@staticmethod` decorators appropriately in your Python classes.

 ## Tasks
 0. `book_class.py`
 - **Objective:** Master Python magic methods by implementing a `Book` class that incorporates constructors (`__init__`, destructors (`__del__`), and the representation methods (`__str__` and `__repr__`).
 - **Task Description:**
   - Create a Python Script named `book_class.py`. In this script, define a `Book` class that uses specific magic methods to enhance it's functionality. This class will model a book with:
        - **Attributes:**
            - `title` (str): The title of the book.
            - `author` (str): The author of the book.
            - `year` (int): The publication year of the book.

        - **Magic Methods:**
            - *Constructor(`__init__`):* Initializes a `Book` instance with `title`, `author`, and `year`.
            - *Destructor(`__del__`)*: Prints `"Deleting (title of the book)"` upon object deletion.
            - *String Representation(`__str__`)*: Returns a string in the format `"(title) by (author), published in (year)"`.
            - *Official Representation(`__repr__`):* Returns a string that would recreate the <span style="color:red;">`Book`</span> instance: `f"Book('{self.title}', '{self.author}', '{self.year}')"`.
### `0-main.py` Test file
```python
from book_class import Book

def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(my_book)  # Expected to use __str__

    # Demonstrating the __repr__ method
    print(repr(my_book))  # Expected to use __repr__

    # Deleting a book instance to trigger __del__
    del my_book

if __name__ == "__main__":
    main()
```
#### *Expected Output*
```md
1984 by George Orwell, published in 1949
Book('1984', 'George Orwell', 1949)
Deleting 1984
```
---

1. `library_system.py`
- **Objective:** Deepen your understanding of inheritance and composition in Python by creating a system that models a library with different types of books.
- **Task Description:** Develop two Python Scripts: `library_system.py` and `main.py`. In `library_system.py`, you'll define a base class `Book` and two derived classes, `EBook` and `PrintBook`, showcasing inheritance. Additionally, implement a `Library` class demonstrating composition by managing a collection of books.
    - Base Class `Book`:
        - Attributes: `title` (str) and `author` (str).
        - Method: `__init__(self, title, author)`

    - Derived Classes `EBook` and `PrintBook`:
        - Both inherit from `Book`.
        - `EBook` has additional attribute `file_size` (int)
        - `PrintBook` additional attribute `page_count` (int)
        - Each derived class should have it's own `__init__` method that properly calls the base class `__init__` while also initializing it's unique attribute.
    - Composition `Library`:
        - *Attributes:*
            - `books` (a list to store instances of `Book`, `EBook`, and `PrintBook`).
        - *Methods:*
            - `add_book(self, book)`: Adds a `Book`, `EBook`, and `PrintBook` instances to the library.
            - `list_books(self)`: Prints details of each book in the library.

- `main.py` file for testing:
```py
from library_system import Book, EBook, PrintBook, Library

def main():
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()

if __name__ == "__main__":
    main()
```
#### *Expected Output:*
```md
Book: Pride and Prejudice by Jane Austen
EBook: Snow Crash by Neal Stephenson, File Size: 500KB
PrintBook: The Catcher in the Rye by J.D. Salinger, Page Count: 234
```
---
2. `polymorphism_demo.py`: Exploring Polymorphism and Method Overriding
- *Objective:* Enhance your understnading of polymorphism in Python by creating a set of classes that demonstrate method overriding and polymorphic behavior.
- *Task Description:* 
    - Define a base class `Shape`.
        - Method: `area(self)`, which simply raises a `NotImplementedError`, indicating that the derived classes need to override this method.
    - Derived class `Rectangle`:
        - Inherits from `Shape`.
        - Attributes:
            - `length` and `width`.
        - Overrides the `area()` method to calculate the rectangle's area using the formula: *length x width*.
    - Derived Class `Circle`:
        - Inherits from `Shape`.
        - Attributes: `radius`
        - Overrides the `area()` method to calculate the circle's area using the formula: *π × radius² (Use `math.pi for π`)

### 2-main.py for Testing
```python
from polymorphism_demo import Shape, Rectangle, Circle
import math

def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()
```

#### *Expected Output*
```md
The area of the Rectangle is: 50
The area of the Circle is: 153.93804002589985
```
---
3. `class_static_methods_demo.py`: Distinguishing Between Class Methods and Static Methods
- *Objective:* Solidify your understanding of class methods and static methods in Python by implementing examples of each in a class, demonstrating their usage and differences
- *Task Description:*
    - Define a class `Calculator` with class and static method:
        - `add(a, b)`: Static method. Returns the sum of two numbers.
        - `multiply(cls, a, b)`: Class method. Returns the product of two numbers. Use `@classmethod` decorator and ensure it prints a class attribute named `calculation_type` before performing the multiplication.
    - Class Attributes:
        - Define a class attribute `calculation_type` with a value of `Arithmetic Operations` that the `multiply` class method will reference.

### `3-main.py` for Testing
```python
from class_static_methods_demo import Calculator

def main():
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()
```

#### *Expected Output*
```md
The sum is: 15
Calculation type: Arithmetic Operations
The product is: 50
```