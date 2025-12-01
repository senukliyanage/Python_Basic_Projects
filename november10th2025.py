'''Shopping Menu System
Concepts: while-else, match-case, if-elif
Description:
Display a shopping menu (add item, view cart, remove item, checkout).
Use while to keep the menu active until the user selects exit.
Use match-case for menu options.
Use if to check for errors like removing an item not in the cart.'''

cart = []
print("Welcome to My Shop!")
while True:
    print("\n Shopping Menu:")
    print("1) Add Item to Cart")
    print("2) View Cart")
    print("3) Remove Item from Cart")
    print("4) Checkout")
    print("5) Exit")
    choice = int(input("Select an option (1-5): "))
    match choice:
        case 1:
            item = input("What would you like to add to your cart?: ")
            if item:
                cart.append(item)
                print(f"{item} has been added to your cart.")
            else:
                print("Invalid item. Please try again.")
        case 2:
            if cart:
                print("Your cart contains:")
                for i, item in enumerate(cart, 1):
                    print(f"{i}. {item}")
            else:
                print("Your cart is empty.")
        case 3:
            if cart:   
                item = input("What would you like to remove from your cart?: ")
                if item in cart:
                    cart.remove(item)
                    print(f"{item} has been removed from your cart.")
                else:
                    print("Item not found in cart.")
            else:
                print("Your cart is empty. Nothing to remove.")
        case 4:
            if cart:
                print("Checking out the following items:")
                for i, item in enumerate(cart, 1):
                    print(f"{i}. {item}")
                print("The total items you are purchasing:", len(cart))
                if input("Confirm checkout? (yes/no:)").lower() == "yes":
                    cart.clear()
                    print("Thank you for your purchase!")
                    break
                else:
                    print("Checkout cancelled.")
                    break
            else:
                print("Your cart is empty. Nothing to checkout.")

        case 5:
            print("Exiting the shop. Have a great day!")
            break
        case _:
            print("Invalid option. Please select a number between 1 and 5.")
else:
    print("Thank you for visiting My Shop!")
