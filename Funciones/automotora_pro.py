automotora = [
    {"Marca": "Nissan", "Valor": 10000000, "Año": 2010, "Stock": 1, "Estado": True}
]

Menu="""
--------MENU --------
[1] Agregar auto
[2] Vender auto
[3] Buscar auto
[4] Actualizar stock
[5] Mostrar autos
[6] Salir
---------------------
"""

def AgregarAuto():
    marca=input("Ingrese la marca del auto: ")
    valor=int(input("Ingrese el valor del auto: "))
    año=int(input("Ingrese el año del auto: "))
    automotora.append({"Marca": marca, "Valor": valor, "Año": año, "Stock": 1, "Estado": True})
    print("Auto agregado con exito")

def VenderAuto(lista_auto, posicion_auto):
    indice = -1
    if 0 <= indice < len(lista_auto):
        auto_borrado = lista_auto.pop(indice)
        return auto_borrado["Marca"]
    else:
        return False


def BuscarAuto(lista_autos, marca_a_buscar):
    for a in lista_autos:
        if a["Marca"]==marca_a_buscar:
            print(f"Producto encontrado --> Marca:{a['Marca']} | Valor:{a['Valor']} | Año:{a['Año']} | Stock:{a['Stock']}")
            return
    print("Producto no encontrado.")

def ActualizarStock():
    MostrarAutos()
    auto_modificar = int(input("A cual auto quiere modifcar el stock?: "))
    nuevo_stock=int(input("Ingrese el nuevo stock: "))
    automotora[auto_modificar-1]["Stock"]=nuevo_stock
    for k in automotora:
        if k["Stock"]<=0:
            k["Estado"]=False
        else:
            k["Estado"]=True
        

def MostrarAutos(lista):
    if len(automotora)==0:
        print("No hay autos para mostrar")
        return
    else:
        c=1
        for i in automotora:
            print(f"\n---- AUTO {c} ----")
            print(f"\nMarca: {i['Marca']}\nValor: ${i['Valor']}\nAño: {i['Año']}\nStock: {i['Stock']} \nEstado: {i['Estado']} \n ")
            c+=1

while True:
    try:
        print(Menu)
        op=int(input("Ingrese una opcion: "))
        match op:
            case 1:
                AgregarAuto()
            case 2:
                vender=int(input("Seleccione el auto que desea vender: "))
                resultado=VenderAuto(automotora, vender)
                if resultado == False:
                    print("Error: Ese numero de auto no existe")
                else:
                    print(f"Venta exitosa Se ha vendio el auto marca: {resultado}")
                VenderAuto()
            case 3:
                buscar = input("Ingrese el nombre del auto: ")
                BuscarAuto(automotora, buscar)
            case 4:
                ActualizarStock()
            case 5:
                MostrarAutos(automotora)
            case 6:
                print("Muchas gracias por preferirnos, vuelva pronto!")
                break
            case _:
                print("Ingrese una opcion valida...")
    except:
        print("ERROR")