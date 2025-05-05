ListaDeAnimales = []
chose = 0

while True:
    print(f"""
1. Agregar animal
2. Ver lista de animales
3. Eliminar animales
4. Salir """)
    
    chose = input("Ingrese que quiere hacer ").lower()
    if chose == "1" or chose == "agregar":
        while True:
            try:
                Mascota=input("Introduce el nombre de la mascota o salir \n")
                if Mascota.lower() == "salir":
                    break
                # Conseguir caracteristicas de la mascota
                TipoPet = input("Que clase de mascota es? \n")
                EdadPet = input("Edad de la mascota \n")
                GenderPet = input("Genero de la mascota M/F \n")
                BreedingPet = input("Castrado Si/No \n").lower()
                Enfermo = input("Esta enfermito? Si/No \n")
                Tamaño = input ("Tamaño Grande/Pequeño/Mediano? \n")

            # Diccionario de esto
                InfoDeLaPet = {
                    "TipoPet": Mascota,
                    "Edadpet": EdadPet,
                    "Genderpet": GenderPet,
                    "BreedingPet": BreedingPet,
                    "Enfermo": Enfermo,
                    "Tamaño": Tamaño
            }
                ListaDeAnimales.append(InfoDeLaPet)
                print(f"Usted acaba de añadir una mascota: '{Mascota}'")
                print("Caracteristicas:", InfoDeLaPet)
                print(f"{ListaDeAnimales}")
            except Exception as e:
                print(f"Error:")
    ########################
    elif chose == "2" or chose == "ver":
        if ListaDeAnimales:
            print(f"----ListaDeAnimales----")
            for Pet in ListaDeAnimales:
                print(f"\nNombre: {Pet['TipoPet']}\n")
                print(f"Edad: {Pet['Edadpet']}\n")
                print(f"Genero: {Pet['Genderpet']}\n")
                print(f"Castrado: {Pet['BreedingPet']}\n")
                print(f"Estado de salud: {Pet['Enfermo']}\n")
                print(f"Tamaño de la mascota: {Pet['Tamaño']}\n")
                print("----------------------------------------")
        else:
            print("Que andas buscando xd")
    #######################       
    elif chose == "3" or chose == "eliminar":
        if ListaDeAnimales:
            print("\n Lista de animales")
            for i, pet in enumerate(ListaDeAnimales,1):
                print(f"{i}. {pet['TipoPet']}")
            try:
                index= int(input("Ingrese el numero de la mascota que quiere eliminar")) - 1
                if index == -1:
                    continue
                elif 0 <= index < len(ListaDeAnimales):
                    RemovePet= ListaDeAnimales.pop(index)
                    print(f"\n Mascota removida: {RemovePet['TipoPet']}")
                else:   
                    print("Numero invalido como yo haciendo ese crud") 
            except ValueError:
                print("Ingrese un numero valido")
        else:
            print("No hay mascotas para eliminar")
    ###########################        
    elif chose == "4" or "salir":
        print("Saliendo del menu")
        break
    else:
        print("Que estas intentando?")
