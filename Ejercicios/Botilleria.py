productos=[

]

def AgregarProducto():
    nombre=input("Ingrese el nombre del producto a agregar: ")
    precio=int(input("Ingrese el precio del producto: "))
    stock=int(input("Ingrese la cantidad de productos: "))
    productos.append({"nombre":nombre, "precio":precio, "stock":stock})

def MostrarBodega():
    if len(productos)==0:
        print("No hay productos en la bodega.")
    else:
        c=1
        for p in productos:
            print(f"{c}. nombre: {p["nombre"]} | precio: ${p["precio"]} | stock: {p["stock"]}")
            c+=1

def VenderProducto():
    MostrarBodega()
    vender=int(input("Cual producto comprara? | seleccione el numero: "))
    cantidad=int(input("Ingrese la cantidad del producto a comprar: "))
    productos[vender-1]["stock"]-=cantidad
    print(f"Venta realizada con exito, el nuevo stock es de: {productos[vender - 1]["stock"]}")
while True:
    try:
        op=int(input("BOTILLERIA \n[1] Agregar producto \n[2] Vender producto \n[3] Mostrar inventario \n[4] Salir \n[INGRESE UNA OPCION]: "))
        match op:
            case 1:
                AgregarProducto()
            case 2:
                VenderProducto()
            case 3:
                MostrarBodega()
            case 4:
                print("Saliendo de la boti!")
                break
            case _:
                print("Ingrese una opcion valida.")
    except:
        print("ERROR")

