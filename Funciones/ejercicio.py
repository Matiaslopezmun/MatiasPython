autos = {
    'A001' : ['Toyota','Corolla',2010,5],
    'A002' : ['Ford', 'Ranger',2019,4],
    'A003' : ['Chevrolet', 'Spark',2022,4],
    'A004' : ['Suzuki', 'Aerio',2005,4],
    'A005' : ['Toyota','Yaris',2015,5],
    'A006' : ['Chevrolet', 'Impala',1950,1],
}
operaciones = {
    'A001' : ['01-01-2024','12-12-2025'],
    'A002' : ['07-08-2024','Pendiente'],
    'A003' : ['09-01-2025','Pendiente'],
    'A004' : ['24-03-2025','Pendiente'],
    'A005' : ['24-03-2024','24-07-2024'],
    'A006' : ['24-03-2024','24-09-2024'],
}

def actualizar_fecha_venta(id_auto, nueva_fecha):
    if id_auto in operaciones:
        operaciones[id_auto][1]=nueva_fecha
        return True
    else:
        return False
autoid=input("Ingrese la ID: ")
fecha_nueva=input("Ingrese la nueva fecha: ")
actualizar_fecha_venta(autoid, fecha_nueva)


def Mostrar_autos():
    for id, datos in operaciones.items():
        print(f"ID: {id} | Datos: {datos}")
Mostrar_autos()


def Busqueda_por_anio(min, max):
    anio=[]
    for id, datos in autos.items():
        if min>datos[2]<max:
            if operaciones[id][1]=="Pendiente":
                anio.append(f"Marca:{datos[0]} | Modelo:{datos[1]} | ID:{id}")
                print("Stock disponible")
    print(anio)
minimo=int(input("Ingrese el minimo: "))
maximo=int(input("Ingrese el maximo: "))
Busqueda_por_anio(minimo, maximo)

def autos_vendidos_por_marca(diccionario, vender_marca):
    total=0
    for id, datos in diccionario.items():
        if operaciones[id][1]!="Pendiente":
            if datos[0]==vender_marca:
                total+=1
    print(f"Marca: {vender_marca} Total: {total}")
vender_marca=input("Ingrese la marca del auto que desea vender: ")