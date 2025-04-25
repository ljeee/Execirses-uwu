:b

Compatibilidad = 0

Pregunta1 = input("Eres aseada? ").lower()
if Pregunta1 == "si":
    Compatibilidad = Compatibilidad
    Pregunta1_2 = input("Te lavas el pelo? ").lower()
    if Pregunta1_2 == "si":
        Pregunta1_3 = input("Cuantos dias a la semana o.o ")
        if Pregunta1_3.isnumeric() and 3 >= int(Pregunta1_3) <= 5:
            Compatibilidad = Compatibilidad + 65
        elif Pregunta1_3.isnumeric() and int(Pregunta1_3) == 6 or 7:
            Compatibilidad = Compatibilidad + 100
        elif Pregunta1_3.isnumeric() and 0 >= int(Pregunta1_3) <= 4:  
            Compatibilidad = Compatibilidad + 1
        else:
            print("Cuantos dias tiene una semana?")
    elif Pregunta1_2 == "no":
        Compatibilidad = Compatibilidad - 100
elif Pregunta1 == "no":
    Compatibilidad = Compatibilidad - 100

Pregunta2 = input("Te sientas recta usualmente Si/No? ").lower()
if Pregunta2 == "si":
    Compatibilidad = Compatibilidad + 100
elif Pregunta2 == "no":
        Compatibilidad = Compatibilidad - 50

Pregunta3 = int(input("Cuantos años tienes? "))
if Pregunta3 >= 22:
    Compatibilidad = Compatibilidad + 100
elif 18 <= Pregunta3 <= 21:
    Compatibilidad = Compatibilidad + 50
elif Pregunta3 <= 17:
    print("Fo")
    exit()


Pregunta4 = input("Chocoramo o Chocoso ").lower()
if Pregunta4 == "chocoramo":
    Compatibilidad = Compatibilidad + 100
elif Pregunta4 == "chocoso":
        Compatibilidad = Compatibilidad - 50
else:
    print("??????????")
        
Pregunta5 = input("Te cepillas los dientes? ").lower()
if Pregunta5 == "si":
    Compatibilidad = Compatibilidad + 100
elif Pregunta5 == "no":
    Compatibilidad = Compatibilidad - 20


Pregunta6 = input("Coca cola? Si/No ").lower()
if Pregunta6 == "si":
    Compatibilidad = Compatibilidad + 100
    if Pregunta6 == "no":
        Compatibilidad = Compatibilidad


Pregunta7 = input("Perros o gatos ").lower()
if Pregunta7 == "perros":
    print("Woaf")
    Compatibilidad = Compatibilidad + 100
elif Pregunta7 == "gatos":
    print("xd")
    Compatibilidad = Compatibilidad + 80


Pregunta8 = input("Quieres tener hijos? ").lower()
if Pregunta8 == "si":
    Pregunta8 = input("Cuantos? ")
    if Pregunta8.isnumeric() and int(Pregunta8) == [1, 2]:
        Compatibilidad = Compatibilidad + 100
        print ("Nice ")
    elif Pregunta8.isnumeric() and int(Pregunta8) >= 3:
        Compatibilidad = Compatibilidad - 50
        print ("Cule granja ")
elif Pregunta8 == "no":
    Compatibilidad = Compatibilidad + 100
    

Pregunta9 = input("Videojuegos o series? V/S/Ambas/Ninguno ").lower()
if Pregunta9 in ["videojuegos", "v", "series", "s"]:
    Compatibilidad = Compatibilidad + 50
elif Pregunta9 == "ambas":
    Compatibilidad = Compatibilidad + 100
elif Pregunta9 == "ninguno":
    Compatibilidad = Compatibilidad - 100
    print("Que aburrida xd")

Pregunta10= input("Te gustan los tatuajes Si/No ").lower()
if Pregunta10 == "si":
    Compatibilidad = Compatibilidad + 100
    Pregunta10 = input("Tienes? ").lower
    if Pregunta10 == "si":
        print("Nice :D")
    elif Pregunta10 == "no":
        Compatibilidad = Compatibilidad
elif Pregunta10 == "no":
    print("Jmm")
    Compatibilidad = Compatibilidad - 100
    

Pregunta11= input("Polita? Si/No ").lower()
if Pregunta11 == "si":
    Compatibilidad = Compatibilidad + 100
elif Pregunta11 == "no":
    print("oks")


Pregunta12= input("Te gustan los pircings? ").lower()
if Pregunta12 == "si":
    Compatibilidad = Compatibilidad + 100
    input("Tienes? ").lower()
    if Pregunta12 == "si":
        Pregunta12 = input("Cuantos? ")
    elif pregunta12 == "no":
        Compatibilidad = Compatibilidad
elif Pregunta12 == "no":
    Compatibilidad = Compatibilidad - 70

print(f"Su compatibilidad es: {Compatibilidad}")

if Compatibilidad >= 1000:
    print("Somos re compatibles")
elif Compatibilidad >= 500:
    print("Podemos trabajar en eso xd")
elif Compatibilidad >=1300:
    print("Almas gemelas xd")
else:
    print("Noup, keep working")
