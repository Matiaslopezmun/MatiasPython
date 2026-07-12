productos=[

]

def AgregarCompletos():
    nombre=input("Ingres el completo que desea agregar: ")
    precio=int(input("Ingrese el valor del producto: "))
    stock=int(input("Ingrese la cantidad de de completos: "))
    productos.append({"nombre":nombre, "precio":precio, "stock":stock})

def MostrarCarta():
    if len(productos)==0:
        print("No hay stock disponible")
    else:
        c=1
        for p in productos:
            print(f"{c}.- Nombre: {p['nombre']} | precio: ${p['precio']} | stock: {p['stock']}")
            c+=1

def VenderCompleto():
    if len(productos) == 0:
        print("No hay productos para vender.")
        return
        
    MostrarCarta()
    seleccion = int(input("¿Cuál producto desea vender? (Ingrese el número): "))

    if productos[seleccion - 1]["stock"] > 0:
        productos[seleccion - 1]["stock"] -= 1 
        print(f"Venta realizada. Nuevo stock: {productos[seleccion - 1]['stock']}")
    else:
        print("Lo sentimos, no queda stock de este producto.")




while True:
    try:
        op=int(input("\nCOMIDA RAPIDA \n[1]. Agregar completo \n[2]. Vender producto \n[3]. Mostrar carta \n[4]. Salir\nSeleccione un producto: "))
        match op:
            case 1:
                AgregarCompletos()
                
            case 2:
                MostrarCarta()
            case 3:
                VenderCompleto()
            case 4:
                print("Muchas gracias por venir.")
            case _:
                print("Ingrese una opcion valida.")

    except:
        print("")