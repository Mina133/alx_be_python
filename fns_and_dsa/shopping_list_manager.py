def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            newItem = input("Enter the item to add: ")
            shopping_list.append(newItem)
            pass
        elif choice == '2':
            itemToRemove = input("Enter the item to remove: ")
            shopping_list.remove(itemToRemove)
            pass
        elif choice == '3':
            print("Shopping List:", shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()