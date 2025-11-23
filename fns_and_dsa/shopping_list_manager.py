"""
"""

def display_menu():
    """Prints the main menu options to the console."""
    print("\n--- Shopping List Manager ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print("---------------")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your Choice (choose 1, 2, 3 or 4): ")

        if choice == '1':
                item = input("Enter the item to add: ").strip().capitalize()
                shopping_list.append(item)
                print(f"'{item}' has been added to the list.")
        elif choice == '2':
                # Print the list to the user, ask them to choose the item
                print("Current Items in the List are: ")
                for i in shopping_list:
                    print(i)
                item_to_remove = input("Enter the item to remove: ").strip().capitalize()
                try:
                    shopping_list.remove(item_to_remove)
                    print(f"'{item_to_remove}' has been removed from the list.")
                except ValueError:
                    print(f"Error: '{item_to_remove}' was not found in the list.")

        elif choice == '3':
            print("\n Current Shopping List:")
            if shopping_list:
                for index, item in enumerate(shopping_list, 1) :
                    print(f"{index}. {item}")
            else:
                print("The list is currently empty!")
            print("---------------")   
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid Choice. Please enter a number between 1 and 4.")

if __name__== "__main__":
    main()