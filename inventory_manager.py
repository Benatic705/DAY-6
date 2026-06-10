inventory = {}

while True:
    print("\nINVENTORY MANAGEMENT TOOL")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Quantity")
    print("4. Delete Product")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        product = input("Enter Product Name: ")
        quantity = int(input("Enter Quantity: "))

        inventory[product] = quantity

        print("Product Added Successfully!")

    elif choice == "2":
        if not inventory:
            print("Inventory Empty")
        else:
            print("\nInventory Items")

            for product, quantity in inventory.items():
                print(product, ":", quantity)

    elif choice == "3":
        product = input("Enter Product Name: ")

        if product in inventory:
            quantity = int(input("Enter New Quantity: "))
            inventory[product] = quantity

            print("Quantity Updated")
        else:
            print("Product Not Found")

    elif choice == "4":
        product = input("Enter Product Name: ")

        if product in inventory:
            del inventory[product]

            print("Product Deleted")
        else:
            print("Product Not Found")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid Choice")

    