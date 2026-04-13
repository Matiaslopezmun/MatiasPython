# # Creando variables

# titulo="Clima de hoy" # String
# diaDelMes=13 # Int
# mes=4 # Int
# temperatura=22.3 # Float
# llueve=False # Boolean

# print(titulo)
# print("temperatura actual:", temperatura, "grados")
# print(diaDelMes, "/", mes)

# if llueve:
#     print("Tiene que llevar un paraguas")
# else:
#     print("Puede llevar polera sin mangas")


# pedir password y pin
# pida al usuario password en palabra que debe ser "temu"
# ademas pida el pin que debe ser 3435
# los dos deben estar correctos para acceder al sistema



# print("Ingrese su password: ")
# input()

# pin=3435
# password="temu"

# if password=="temu":
#     print("Acceso correcto")
#     int(input("Ahora ingrese su pin: "))

#     if pin==3435:
#         print("Haz ingresado correctamente")
# else:
#     print("Acceso denegado")





Ingresos=int(input("Agrege sus ingresos: "))
print("")
print("Ingrese su nivel de educacion: ")
print("1. Basica")
print("2. Media")
print("3. Superior")
Educacion=int(input("Seleccione una opcion: "))

print("")
print("Ingrese su nacionalidad: ") 
print("1. Chilena")
print("2. Otra")
nacionalidad=int(input("Seleccione una opcion: "))
credito=0

if Ingresos>500000 and Ingresos<1000000:
    credito=credito+300000
elif Ingresos>1000000 and Ingresos<1500000:
    credito=credito+650000
elif Ingresos>1500001:
    credito=credito+1000000
else:
    print("Usted no es apto para ningun credito")

if Educacion==1:
    credito=credito*1
elif Educacion==2:
    credito=credito*1.3
elif Educacion==3:
    credito=credito*1.5
else:
    print("")

if nacionalidad==1:
    credito=credito+300000

else:
    print("No tiene bono por nacionalidad")

print("")
print("El credito al cual usted puede acceder es:", credito, "pesos")


