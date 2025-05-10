#La ratona dijo no try's
#And clave in clave

Inventory = {    
    "book a": {"price": 10.99, "Quantity": 5},
    "book b": {"price": 15.50, "Quantity": 3},
    "book c": {"price": 7.25, "Quantity": 10},
    "book d": {"price": 12.00, "Quantity": 0},
    "book e": {"price": 20.00, "Quantity": 2}
}

#Add books
def AddBooks():
    print("Introduce Books")
    while True:
        Name = input("Introduce the name of the book(or exit for go to the menu): ").lower()
        if Name in ["salir", "exit", "end"]:
            return
        elif Name in Inventory:
            print("Este contacto ya existe")
            return
        elif not Name:
            print("You're introducing no name")
        else:
            print(f"Book {Name.title()} inserted")
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
                print(f"Price of {Name.title()} inserted")
                break
        else:
            print("You know how to follow instructions?")
    while True:
        Quantity = input("Enter the amount to be added to stock: ")
        if any([not Quantity.strip(), not Quantity.isdigit()]):  # Algún error: vacío o no dígitos
            print("La cantidad no puede estar vacia" if not Quantity else "No deberian ser numeros?")
        else:
            Quantity = float(Quantity)
            if Quantity < 0:
                print("No puede ser menor los va regalar antes de sacarlos?")
            else:
                print(f"Price of {Name} inserted")
                break
    Inventory[Name] = {"price": Price, "Quantity": Quantity}

#Search books in the inventory
def SearchBooks():
    while True:
        LookinForBook = input("Introduce the name of the book what are you looking for: ").lower().strip()
        if LookinForBook in Inventory:     
            DataBook = Inventory[LookinForBook]   
            print("==========================================")
            print(f"Name of book: {LookinForBook.title()}, Price: {DataBook['price']}, Quantity: {DataBook['Quantity']}")
            print("==========================================")
            break
        elif not LookinForBook:
            print("El nombre no puede estar vacío.")
        else:
            print("That book isn't here")
            break

#Uptadte prices
def UpdatePrices():
    WatchallBooks()
    while True:
        LookForBook = input("Introduce el libro que quieres updatear: ").lower().strip()
        if not LookForBook:
            print("El nombre no puede estar vacío.")
        elif LookForBook in ["salir", "exit", "end"]:
            print("Exiting...")
            return
        else: 
            if LookForBook in Inventory:
                while True:
                    ChangePrice = input("Cual es el precio que quiere updatear?").strip()
                    if ChangePrice.isdigit():
                        ChangePrice = float(ChangePrice)
                        if ChangePrice < 0:
                            print("No puede ser menor a 0 o los va regalar?")
                        else:
                            Inventory[LookForBook]['price'] = ChangePrice
                            print(f"The price of '{LookForBook.title()}' has been updated to {ChangePrice:.2f}.")
                            return
                    else:
                        print("You know how to follow instructions? Introduce a number")
            else:
                print(f"The book introduced is not in the inventory.")

#When you want to see all the books
def WatchallBooks():
    if not Inventory:
        print("No books in the inventory")
        return
    print("This is the list of books in the inventory")
    for book in Inventory.items():
        print(f"Book: {book[0].title()}")

def DeleteBooks():
    if Inventory:
        print("Inventory:")
        for book in Inventory:
            print(f"-> {book.title()}")
        while True:
            Eliminar = input("Enter the name of the book to delete or type 'exit' to return to the menu: ").strip().lower()
            if Eliminar in ["salir", "exit"]:
                print("Exiting...")
                break
            elif Eliminar in Inventory:
                del Inventory[Eliminar]
                print(f"Book '{Eliminar.title()}' removed")
                break
            elif not Eliminar:
                print("The name cannot be empty.")
            else:
                print("The book is not in the inventory. Please try again")
    else:
        print("The inventory is empty")

#Stock Total Value
def TotalPrices():
    if not Inventory:
        print("No books in the inventory")
    else:
        TotalPricess= sum(item["price"] * item["Quantity"] for item in Inventory.values())
        print(f"The total value is: {TotalPricess:.2f}")

#Modify books
def Modify():
    WatchallBooks()
    if not Inventory:
        return
    while True:
        Modify = input("Libro que quieres modificar: ").strip().lower()
        if not Modify:
            print("El nombre no puede estar vacío.")
            continue
        elif Modify in ["salir", "exit", "end"]:    
            print("Exiting...")
            return
        elif Modify in Inventory:
            while True:
                NewName = input("Introduce el nuevo nombre: ").strip().lower()
                if not NewName:
                    print("El nuevo nombre no puede estar vacío.")
                elif NewName in Inventory:
                    print("Este libro ya existe en el inventario.")
                else:
                    Inventory[NewName] = Inventory.pop(Modify)
                    print(f"Book '{Modify}' renamed to '{NewName}'.")
                    return
        else:
            print("El libro no está en el inventario. Por favor, inténtalo de nuevo.")

def VertodoElInventario():
    if Inventory:
        print("This is the list of books in the inventory")
        for book, data in Inventory.items():
            print(f"Book: {book.title()}, Price: {data['price']}, Quantity: {data['Quantity']}")
    else:
        print("No books in the inventory")
        return
#Menu(English)
def Menu():
    while True:
        print("1. Add books")
        print("2. Search books")
        print("3. Update prices")
        print("4. Total value of the stock")
        print("5. List of books")
        print("6. Delete books")
        print("7. Modify name books")
        print("8. VertodoElInventario")
        print("9. Salir | Exit | Cerrar | Close | End | Finish")
        option = input("What you wantxd: ").lower()
        match option:
            case "1" | "add" | "add books" | "addbooks":
                AddBooks()
            case "2" | "search" | "search books" | "searchbooks":
                SearchBooks()
            case "3" | "updateprices" | "update" | "update prices":
                UpdatePrices()
            case "4" | "total" | "total value" | "totalvalue":
                TotalPrices()
            case "5" | "list"  | "list of books" | "listofbooks":
                WatchallBooks() 
            case "6" | "delete" | "delete books" | "deletebooks":
                DeleteBooks()
            case "7" | "modify" | "modificar":
                Modify()
            case "8" | "vertodoinventario" | "vertodoelinventario":
                VertodoElInventario()
            case "9" | "salir" | "exit" | "cerrar" | "close" | "end" | "finish":
                break
            case _:
                print("Invalid option, please try again.")   

Menu()
