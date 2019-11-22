# Ben Lizza
# 11/20/19
# Driver for the Textbook module
# create two textbooks that the user will input. Have a menu to let the user pick one of three things to do with the textbook

from Textbook_module import Textbook

book1 = Textbook("Writing Express", "Thomas", "Smith", 54, 3, 3378729, 200, 45)
book2 = Textbook("Math Equations", "Frank", "Waterman", 38, 2, 2349322, 345, 80)

menu = 0

while menu != 4:
    print("What would you like to do, please select from the menu:")
    print("1. Add to inventory")
    print("2. Deduct from inventory")
    print("3. Modify the price of the book")
    print("4. Quit the program")

    # Something wrong with this?  What data type does input return?  What data type do you need?
    menu = input()

    if menu == 1:
        print("Which book would you like to use?")
        choice = input()
        if choice == 1:
            quantity = int(input("How many books would you want to add to the inventory?"))
            book1.add_inventory(quantity)
            print("The quantity in inventory is now ") + str(book1.quantity) + "\n\n"
        else:
            quantity = int(input("How many books would you like to add to the inventory?"))
            book2.add_inventory(quantity)
            print("The quantity of the inventory is now ") + str(book2.quantity) + "\n\n"
    elif menu == 2:
        print("Which book would you like to use?")
        choice = input()
        if choice == 1:
            qty = int(input("How many would you like to remove?"))
            result = book1.deduct_inventory(qty)
            if result == 0:
                print("The quantity in the inventory is now ") + str(book1.quantity) + "\n\n"
            else:
                print("The quantity in the inventory is now ") + str(book1.quantity) + "\n\n"
        elif choice == 2:
            qty = int(input("How many would you like to remove?"))
            result = book1.deduct_inventory(qty)
            if result == 0:
                print("The quantity in the inventory is now ") + str(book2.quantity) + "\n\n"
            else:
                print("The quantity in the inventory is now ") + str(book2.quantity) + "\n\n"
    elif menu == 3:
        print("Which book, 1 or 2?")
        choice = input()
        if choice == 1:
            price = float(input("What will the new price be? "))
            book1.price = price
            print("The price of " + book1.title + "has been changed to " + str(book1.price) + "\n\n")
        elif choice == 2:
            price = float(input("What will the new price be? "))
            book2.price = price
            print("The price of " + book2.title + "has been changed to " + str(book2.price) + "\n\n")
    elif menu == 4:
        print("Thank you for using this system!")

