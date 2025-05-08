Contacts = {}

def AgregarPendejo():
    while True:
        try:
            Name = input("Introduce el nombre")
            if Name in Contacts:
                print("Este contacto ya existe")
                continue
            else:
                print(f"Contacto {Name}, Introducido")
                break
        except Exception as e:
            print(f"Error inesperado: {e}")

    while True:
        try:
            Phone = input("Introduce el nombre")
            if Phone in Contacts:
                print("Ya tienes alguien con este numero")
            else:
                print(f"Telofono de {Name}, Introducido")
                break
        except Exception as e:
            print(f"Error inesperado: {e}")

    while True:
        try:
            Mail = input("Introduce el nombre")
            if Mail in Contacts:
                print("Este contacto")
            else:
                print(f"Mail de {Name}, Introducido")
                break
        except Exception as e:
            print(f"Error inesperado: {e}")
            
    while True:
        try:
            Nickname = input("Introduce el apodo del contacto")
            if Nickname in Contacts:
                print("Este contacto")
            else:
                print(f"Nickname de {Name} Introducido")
                break
            Contacts[Name] = {"tele": Phone, "correo": Mail, "Apodo": Nickname}
            print(f"{Contacts}")
        except Exception as e:
            print(f"Error inesperado: {e}")    
    
    
    

### Menu
chose = 0
while True:
    print(f"""
1. Agregar nuevo contacto
2. Buscar contacto
3. Eliminar contacto
4. Modificar contacto
5. Ver contactos
5. Salir """)
    chose = input("Ingrese que quiere hacer: ").lower()
    if chose == "1" or chose == "agregar":
        AgregarPendejo()
    elif chose == "2" or chose == "ver":
        VerEstudiante()
    elif chose == "3" or chose == "eliminar":
        EliminarEstudiante()
    elif chose == "4" or chose == "modificar":
        ModificarCalificacion()
    elif chose == "5" or chose == "salir":
        print(f"-"*30)
        print("Saliending....")
        break
    else:
        print("???????")
    
