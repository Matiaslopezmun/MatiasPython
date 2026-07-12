productos=[
    {"nombre": "Lavadora", "stock": 10, "precio": 300000, "estado": True},
    {"nombre": "Calefactor", "stock": 20, "precio": 50000, "estado": True},
    {"nombre": "Cocina", "stock": 0, "precio": 370000, "estado": False}    
]

def AgregarProducto():
    nombre=input("Ingrese el nombre del producto: ")
    stock=int(input("Ingrese la cantidad de stock disponible: "))
    precio=int(input("Ingrese el precio del producto: "))
    estado=True
    productos.append({"nombre":nombre, "stock":stock, "precio":precio, "estado":estado})
    
def BuscarProducto():
    buscar=input("Ingrese el nombre del producto que desea buscar: ")
    if [productos]["nombre"]==buscar:
        print("Producto no encontrado.")
    else: 
        print("Producto encontrado")

def EliminarProducto():
    MostrarProductos()
    eliminar=int(input("Seleccione un producto a eliminar (nombre del producto): "))
    productos.pop(eliminar-1)
    print("Producto eliminado con exito.")

def ActualizarDisponibilidad():
    for k in productos:
        if ["stock"]<=0:
            estado=False
        else:
            estado=True

def MostrarProductos():
    if len(productos)==0:
        print("No hay productos disponibles.")
    else:
        for a in productos:
            print(f"=== LISTA DE PRODUCTOS === \n \nnombre: {a["nombre"]} \nstock: {a["stock"]} \nprecio: ${a["precio"]} \nestado: {a["estado"]} \n********************************************")
            
def MenuPrincipal():
    while True:
        try:
            while True:
                op=int(input(f"=====MENU PRINCIPAL===== \n[1] Agregar producto \n[2] Buscar producto \n[3] Eliminar producto \n[4] Actualizar disponibilidad \n[5] Mostrar productos \n[6] Salir \nSeleccione una opcion: "))
                match op:
                    case 1:
                        AgregarProducto()
                    case 2:
                        BuscarProducto()
                    case 3:
                        EliminarProducto()
                    case 4:
                        ActualizarDisponibilidad()
                    case 5:
                        MostrarProductos()
                    case 6:
                        print("Gracias por usar el sistema. Vuelva Pronto")
                        break
                    case _:
                        print("Ingrese una opcion correcta.")

        except:
            print("ERROR")


MenuPrincipal()


        
