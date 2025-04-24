### LF Multiplo de 3, 5 y varios ###
Numero= float(input("Escriba un numero"))
# Condiciones
if Numero % 5 == 0 and Numero % 3 == 0:
    print("El numero es multiplo de 3 y 5")
elif Numero % 3 == 0:
    print("El numero es multiplo de 3")
elif Numero % 5 == 0:
    print("El numero es multiplo de 5")
else:  
    print("El numero no es multiplo de 3 ni de 5")

### Invertir valores IDK ###
a = float(input("Dame dame un numero "))
b = float(input("Dame el otro uwu "))
print(f"Sus numeros son {a}, y {b}")
a,b = b, a
print (f"Sus numeros invertidos son {a}, {b}")

### Invertir num 3 cifras y separar en centenas, decenas y unidades ###
numeros = int(input("dame un numero de 3 cifras"))
# Transforma la variable numeros en caracteres, la enlista y lee la lista hacia atras 
inver = int(str(numeros)[::-1])
print(f"el numero es" + str(inver))

centena = int(inver) //100
Decena = (int(inver) % 100) // 10
Unidades = int(inver) % 10
print(f"estas son tus centenas:{centena}\nestas tus decenas: {Decena}\nestas tus unidades: {Unidades}")

###  Calculo de horas, minutos y segundos restantes ###

numero = int(input("dime un numero para el calculo"))
hora = int(numero) // 3600
minutos = int(numero) %3600 // 60
segundos = int(numero) % 60
print (f"tienes {hora} horas, {minutos} minutos y {segundos} segundos")

### Fecha de nacimiento en varios formatos , (zfill rellena los slots vacios con ceros) ###

dd = int(input("dame el numero del mes en el que nacimiento " ))
mm = int(input("dame el dia en que naciste " ))
aaaa = int(input("dame el año en que naciste " ))

dd = str(dd).zfill(2)
mm = str(mm).zfill(2)

print(f" Naciste el {dd}/{mm}/{aaaa} \n La fecha al contrario {aaaa}-{mm}-{dd}")

### Tempetura gringa a normal :b ###

Temperatura = input("Dame tu temperatura en Fahrenheit: ")

if Temperatura.replace('.', '', 1).isdigit() or (Temperatura[0] == '-' and Temperatura[1:].replace('.', '', 1).isdigit()):
    Temperatura = float(Temperatura)  # Convertir a float si es un número válido
    temperatura_c = (Temperatura - 32) / 1.8
    print(f"Su temperatura en Fahrenheit: {Temperatura} \nSu temperatura en Celsius: {temperatura_c}")
else:
    print("La temperatura se mide con números, ¿no?")

### Calculo de la jubilacion y condicionales ###

Edad = int(input("Escriba su edad "))
Sexo = input("Escriba su sexo (H/M) ").upper()

if Sexo == "H":
    if Edad >= 65:
        print("Usted es un hombre jubilado")
    elif Edad < 65:
        print("Usted es un hombre no jubilado")
elif Sexo == "M":
    if Edad >= 60:
        print("Usted es una mujer jubilada")
    elif Edad < 60:
        print("Usted es una mujer no jubilada")
else:
    print("Sexo no valido")

### Ratbuzz ###

numero = int(input("dame un numero "))

if numero % 5 == 0 and numero % 3 == 0:
    print ("Both: FizzBuzz")
elif numero % 5 == 0:
    print ("Buzz Multiplo de 5 :b")
elif numero % 3 == 0:
    print ("Fizz Multiplo de 3 :o")
else:
    print (numero)

### Solicitar un número de 4 cifras al usuario###
numero = input("Introduce un número de 4 cifras: ")
#Verificar que el número tenga exactamente 4 cifras
if len(numero) == 4 and numero.isdigit() and not numero.startswith("0"):
#Extraer los dígitos y agruparlos de dos en dos
    pares = [numero[:2], numero[2:]]
#Imprimir los pares separados por coma
    print(",".join(pares))
else:
    print("Por favor, introduce un número válido de 4 cifras.")
    
    
