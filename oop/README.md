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
 1. `book_class.py`
 - Task Description:
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

2. 