Variable = [
    {'Nombre': 'Jeferson', 'Edad': '20', 'Calificación': '100', 'Clan': 'Linux'},
    {'Nombre': 'Kain', 'Edad': '22', 'Calificación': '100', 'Clan': 'Linux'},
    {'Nombre': 'Toph', 'Edad': '23', 'Calificación': '90', 'Clan': 'Loveplace'},
    {'Nombre': 'Yoru', 'Edad': '25', 'Calificación': '100', 'Clan': 'Loveplace'},
    {'Nombre': 'Test', 'Edad': 'Hay que preguntarle', 'Calificación': 'Unknown', 'Clan': 'Unknown'},
]

### Agregar Estudiante

def AgregarEstudiante():
            while True:
                try:
                    Nombres = input("Nombre del estudiante que va agregar o salir: \n-")
                    if Nombres == "salir":
                        break
                    # Comprobar si el nombre esta vacioexiste
                    elif Nombres.strip() == "" or Nombres in Variable:
                        print("El nombre ya existe, No puede estar vacio, elija otro")
                    else:
                        print("Nombre introducido correctamente")
                    # Conseguir edad
                    while True:
                        Edad = input("Edad del estudiante: ")
                        if Edad.isdigit():
                            break
                        else:
                            print("La edad debe ser un número. Inténtelo nuevamente.")
                    while True:
                        Califacion = input("Calificación del estudiante: ")
                        if Califacion.isdigit():
                            Califacion = int(Califacion)
                            if 1 <= Califacion <= 100:
                                break
                            else:
                                print("La calificación debe estar entre 0 y 100. Inténtelo nuevamente.")
                        else:
                            print("La calificación debe ser un número. Inténtelo nuevamente.")
                    #Conseguir clan
                    Clan= input("!Clan del estudiante Linux/Loveplace/Ghosling/Hopper! \n-")
                    if Clan.strip() == "":
                        print("El clan no puede estar vacio")
                        continue
                    else:
                        print(f"Clan introducido correctamente {Clan}")
                    ### Diccionario
                    InfoEstudiante = {
                        "Nombre": Nombres,
                        "Edad": Edad,
                        "Calificación": Califacion,
                        "Clan": Clan,
                    }
                    Variable.append(InfoEstudiante)
                    print(f"Estudiante {Nombres} agregado correctamente.")
                except Exception as e:
                    print(f"¡Error! Intentelo correctamente")

### Ver lista de estudiantes

def VerEstudiante():
    if Variable:
        print("----------Lista de estudiantes--------\n")
        for student in Variable:
            print(f"Estudiante: {student['Nombre']}")
            print(f"Edad: {student['Edad']}")
            print(f"Calificacion: {student['Calificación']}")
            print(f"Clan: {student['Clan']}")
            print("-"*30)
    else:
        print("Wtf???")

### Eliminar Estudiante

def EliminarEstudiante():
    if Variable:
        print("Lista de estudiantes")
        for i, studentt in enumerate(Variable,1):
            print(f"{i}. {studentt['Nombre']}")
        Eliminar = input("Que estudiante quiere eliminar o salir: \n-")
        if Eliminar.lower() == "salir":
            print("-" * 30)
            print("Saliendo....")
            return
        try:
            #Try to delete by index
            index = int(Eliminar) - 1
            if 0 <= index < len(Variable):
                removed_student = Variable.pop(index)
                print(f"Estudiante {removed_student['Nombre']} eliminado correctamente.")
        except ValueError:
            for studentt in Variable:
                if studentt['Nombre'] == Eliminar:
                    Variable.remove(studentt)
                    print(f"Eliminando a {studentt['Nombre']}")
                    return
                        
### Modificar Calificacion
def ModificarCalificacion():
    if Variable:
        print("Lista de estudiantes")
        VerEstudiante()
        Modificar = input("Que estudiante quiere modificar o salir: \n-")
        for student in Variable:
            if student['Nombre'] == Modificar:
                while True:
                    try:
                        Calificacion = int(input("Ingrese la nueva calificación del estudiante: "))
                        if 0 <= Calificacion <= 100:
                            student['Calificación'] = Calificacion
                            print(f"Calificación de {Modificar} modificada correctamente a {Calificacion}.")
                            return
                        else:
                            print("La calificación debe estar entre 1 y 100. Inténtelo nuevamente.")
                    except Exception as e:
                        print(f"¡Error! Inténtelo correctamente.")
            

### Menu
chose = 0
while True:
    print(f"""
1. Agregar Estudiante
2. Ver lista de estudiantes
3. Eliminar estudiantes
4. Modificar calificación
5. Salir """)
    
    chose = input("Ingrese que quiere hacer: ").lower()
    if chose == "1" or chose == "agregar":
        AgregarEstudiante()
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

