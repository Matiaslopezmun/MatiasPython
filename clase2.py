# Ejemplo y explicacion de for

# for i in range(3):
#     print(i+1)


# Pedir un numero al usuario
# Mostrar un saludo esa cantidad de veces


# n1=int(input("Ingrese un numero: "))

# for i in range(n1):
#     print(i+1,"Hola como estas")

# Pedir un numero al usuario y mostrar la tabla de multiplicar de ese numero hasta el 10

# num=int(input("Ingrese un numero: "))

# for i in range(10):
#     print(num, "x" ,  i+1, "=", num*(i+1))


# Pedir un numero al usuario y mostrar la suma desde el 1 hasta ese numero

# num=int(input("Ingrese un numero: "))
# suma=0

# for i in range (num):
#     suma=suma+i+1

# print("El resultado de la suma es:", suma)


# Pedir la cantidad de notas al usuario
# Luego pedir cada nota indivi
# Calulcar el promedio de todas las notas
# Mostrar si aprueba o no

notas=int(input("Ingrese la cantidad de notas: "))
suma=0

for i in range(notas):
    n=float(input(f"Ingrese la nota: "), i+1)
    suma=suma+n
    prom=suma/notas

    if prom>4:
        print("Usted apruba y su promedio es: ",prom)

    else:
        print("Usted a reprobado y su promedio es: ", prom)


# nombre=input("ingrese su nombre: ")
# vocales=0
# consonantes=0

# for i in nombre:
#     print(i)    
#     if i in "aeiouAEIOU":
#         vocales=vocales+1
#     elif i in " ":
#         print(" ")
#     else:
#         consonantes=consonantes+1

# print("La cantidad de vocales es: ",vocales, "y la cantidad de consonantes es: ",consonantes)


# Pida la cantida de alumnos
# Pida cada cantidad de notas x alumno
# Saque el promedio y muestre si aprueba o no
