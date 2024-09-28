

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
        choice = int(input("Enter your choice: "))

        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            pass
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter the item to remove ")
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print("Sorry but the item is not found in your shopping list.")
            pass
        elif choice == '3':
            # Display the shopping list
            print(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

choose = 'y'

while  choose == 'y':
    main()
    choose = input("Do you want to go back to your shopping list? if yes type 'y' else type any other key to exit.").lower()
