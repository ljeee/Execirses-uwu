Variable = [
    {'Nombre': 'Jeferson', 'Edad': '20', 'Calificación': '100', 'Clan': 'Linux'},
    {'Nombre': 'Kain', 'Edad': '22', 'Calificación': '100', 'Clan': 'Linux'},
    {'Nombre': 'Toph', 'Edad': '23', 'Calificación': '90', 'Clan': 'Loveplace'},
    {'Nombre': 'Yoru', 'Edad': '25', 'Calificación': '100', 'Clan': 'Loveplace'}
]
chose = 0

while True:
    print(f"""
1. Agregar Estudiante
2. Ver lista de estudiantes
3. Eliminar estudiantes
4. Salir """)
    
    chose = input("Ingrese que quiere hacer ").lower()
    if chose == "1" or chose == "agregar":
        while True:
            try:
                Nombres = input("Nombre del estudiante que va agregar o salir ")
                if Nombres == "salir":
                    break
                #Conseguir info de los estudiantes
                Edad = input("Edad del estudiante: ")
                Califacion = input("Calificación del estudiante ")
                Clan= input("Clan del estudiante ")

                ### Diccionario
                InfoEstudiante = {
                    "Nombre": Nombres,
                    "Edad": Edad,
                    "Calificación": Califacion,
                    "Clan": Clan,
            }
                Variable.append(InfoEstudiante)
                print(f"{Nombres}")
                print(f"{Variable}")
            except Exception as e:
                print(f"Error:")
    elif chose == "2" or chose == "ver":
        if Variable:
            print("----------Lista de estudiantes--------\n")
            for student in Variable:
                print(f"Estudiante: {student['Nombre']}")
                print(f"Edad: {student['Edad']}")
                print(f"Calificacion: {student['Calificación']}")
                print(f"Clan: {student['Clan']}")
        else:
            print("Wtf???")
    elif chose == "3" or chose == "eliminar":
        if Variable:
            print("Lista de estudiantes")
            for i, studentt in enumerate(Variable,InfoEstudiante,1):
                print(f"{i} . {studentt['Nombre']}")
                try:
                    Index = int(input("Cual desea eliminar"))
                    if Index == 0:
                        continue
                    elif 1 <= Index <= len(Variable):
                        RemoveStundent = Variable.pop(Index - 1)
                        print(f"Este estudiante ha sido eliminado: {RemoveStundent['Nombre']}")
                    else:
                        print("Índice fuera de rango")
                except ValueError:
                    print("?????")
        else:
            print("?????")
    elif chose == "4" or chose == "salir":
        print("Saliending....")
        break
    else:
        print("???????")
