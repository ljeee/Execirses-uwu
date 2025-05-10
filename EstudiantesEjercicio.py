Inventory = {
    "A": {"price": 1599, "Quantity": 10},
    "B": {"price": 9099, "Quantity": 5},
    "C": {"price": 2000, "Quantity": 2},
    "D": {"price": 7050, "Quantity": 8},
    "E": {"price": 12075, "Quantity": 4},
}

#Add books
def AddBooks():
    print("Books")
    while True:
        Name = input("Introduce el nombre(or exit for go to the menu): ")
        if Name in Inventory:
            print("Este contacto ya existe")
        elif Name.lower() in ["salir", "exit", "end"]:
            Menu()
            return
        elif not Name:
            print("You're introducing no name")
        else:
            print(f"Book {Name} inserted")
            break
    while True:
        Price = input("Introduce the price: ")
        if not Price:
            print("La cantidad no puede estar vacia")
        if Price.isdigit():
            Price = float(Price)
            if Price < 0:
                print("No puede ser menor a 0 o los va regalar?")
            else:
                print(f"Price of {Name} inserted")
                break
        else:
            print("You know how to follow instructions?")
    while True:
        Quantity = input("Enter the amount to be added to stock: ")
        if not Quantity:
            print("La cantidad no puede estar vacia")
        if Quantity.isdigit():
            Quantity = float(Quantity)
            if Quantity < 0:
                print("No puede ser menor los va regalar antes de sacarlos?")
            else:
                print(f"Price of {Name} inserted")
                break
    Inventory[Name] = {"price": Price, "Quantity": Quantity}
    print(f"Inventory updated: {Inventory}")

#Search books in the inventory
def LookingForBooks():
    print("Introduce el libro que quieres buscar: ")
    LookinForBook = input("Introduce the name of the book what are you looking for: ")
    if LookinForBook in Inventory:     
        DataBook = Inventory[LookinForBook]   
        print("==========================================")
        print(f"Name of book: {LookinForBook}, Price: {DataBook['price']}, Quantity: {DataBook['Quantity']}")
        print("==========================================")
    else:
        print("That book isn't here")


#Uptadte prices
def UpdatePrices():
    print("This is the list of books in the inventory")
    WatchallBooks()
    LookForBook = input("Introduce el libro que quieres updatear: ")
    if LookForBook in Inventory:
        while True:
            ChangePrice = float(input("Cual es el precio que quiere updatear?"))
            if ChangePrice < 0:
                print("No puede ser menor a 0 o los va regalar?")
            else:
                Inventory[LookForBook]['price'] = ChangePrice
                print(f"The price of '{LookForBook}' has been updated to {ChangePrice}.")
                break
    else:
        print(f"The book '{LookForBook}' is not in the inventory.")

#When you want to see all the books
def WatchallBooks():
    print("This is the list of books in the inventory")
    if not Inventory:
        print("No books in the inventory")
        return
    for book, data in Inventory.items():
        print(f"Book: {book}")
    

#Stock Total Value
def TotalPrices():
    if not Inventory:
        print("There aren't books")
    else:
        TotalPricess= sum(item["price"] * item["Quantity"] for item in Inventory.values())
        print(f"The total value is: {TotalPricess:.2f}")

#Menu(English)
def Menu():
    while True:
        print("1. Add books")
        print("2. Search books")
        print("3. Update prices")
        print("4. Total value of the stock")
        print("5. List of books")
        print("6. Salir | Exit | Cerrar | Close | End | Finish")
        option = input("What you wantxd: ").lower()
        match option:
            case "1" | "add" | "add books" | "addbooks":
                AddBooks()
                continue
            case "2" | "search" | "search books" | "searchbooks":
                LookingForBooks()
            case "3" | "updateprices" | "update" | "update prices":
                UpdatePrices()
            case "4" | "total" | "total value" | "totalvalue":
                TotalPrices()
            case "5" | "list"  | "list of books" | "listofbooks":
                WatchallBooks() 
            case "6" | "salir" | "exit" | "cerrar" | "close" | "end" | "finish":
                break    

Menu()
