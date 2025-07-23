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
            itemInput = input("Enter the name of item to add to shopping list: ").lower()
            shopping_list.append(itemInput)
        elif choice == '2':
            itemInput = input("Enter the name of item to remove: ").lower()
            indexOfItem = shopping_list.index(itemInput)
            shopping_list.pop(indexOfItem)
            print(f"{itemInput} removed successfully.")
        elif choice == '3':
            print("Your shopping list")
            for index, item in enumerate(shopping_list, start=1):
                print(f"{index}. {item.capitalize()}")
            print("---------------------------")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()