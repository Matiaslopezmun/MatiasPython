autos=[

]

def AgregarAuto():
    patente=int(input("Ingrese la patente del auto: "))
    marca=input("Ingrese la marca del auto: ")
    minutos=int(input("Ingrese los minutos de estacionamiento: "))
    autos.append({"patente":patente, "marca":marca, "minutos":minutos})
    print("Auto ingresado con exito.")

def VerAutos():
    if len(autos)==0:
        print("No hay autos registrados.")
    else:
        c=1
        for a in autos:
            print(f"{c}. patente: {a["patente"]} | marca: {a["marca"]} | minutos: {a["minutos"]}")
            c+=1

def SumarTiempo():
    VerAutos()
    seleccion=int(input("Ingrese el auto al que le quiere sumar tiempo: "))
    autos[seleccion-1]["minutos"]+=30
    print("Se han sumado 30 minutos por demorar mas.")

while True:
    try:
        op=int(input(f"PARKING \n[1] Ingresar auto \n[2] Ver autos \n[3] Sumar tiempo \n[4] Salir. \nINGRESE UNA OPCION: "))
        match op:
            case 1:
                AgregarAuto()
            case 2:
                VerAutos()
            case 3:
                SumarTiempo()
            case 4:
                print("SALIENDO DEL SISTEMA DE PARKING...")
                break
            case _:
                print("Ingrese una opcion valida.")
    except:
        print("ERROR")