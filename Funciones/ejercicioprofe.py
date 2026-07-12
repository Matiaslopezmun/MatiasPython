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

def autos_vendidos_por_marca(marca):
    total_vendidos=0

    for id_auto, datos in autos.items():
        marca_auto=datos[0]

        if marca_auto.lower()==marca.lower():

            fecha_venta=operaciones[id_auto][1]

            if fecha_venta!="Pendiente":
                total_vendidos+=1
    print(f"Total de autos vendidos de la marca {marca}: {total_vendidos}")

def busqueda_por_anio(anio_min, anio_max):
    resultados=[]

    for id_auto, datos in autos.items():
        marca=datos[0]
        modelo=datos[1]
        anio=datos[2]

        if anio_min<=anio<=anio_max:
            if operaciones[id_auto][1]=="Pendiente":
                texto=f"{marca} {modelo}--{id_auto}"
                resultados.append(texto)

    if resultados:
        resultados.sort()
        print("\n--- Vehiculos disponibles en ese rango ---")
        for auto in resultados:
            print(auto)
        else:
            print("no se encontraron vehiculos disponibles en ese rango de añós.")

try:
    anio_min=int(input("Ingrese el año minimo: "))
    anio_max=int(input("Ingrese el año maximo: "))
except ValueError:
    print("Error: Debe ingresar estrictamente numeros enteros para los añós.")

def actualizar_fecha_venta(id_auto, nueva_fecha):
    if id_auto in operaciones:
        operaciones[id_auto][1]=nueva_fecha
        return True
    else:
        return False
    
continuar="s"
while continuar.lower()=="s":
    id_ingresado=input("Ingrse la ID del auto a actualizar: ").upper()
    fecha_ingresada=input("Ingrese la nueva fecha de venta (ej: 12-07-2026): ")

    exito=actualizar_fecha_venta(id_ingresado, fecha_ingresada)

    if exito:
        print("Exito! La fecha de venta se actualizo correctamente.")
    else:
        print("Error: El identificador ingresado no existe en el sistema.")
    
    continuar=input("Desea actualizar otro vehiculo (s/n): ")

def validar_texto(texto):
    return len(str(texto).stri()) > 0
def validar_anio(anio):
    try:
        return int(anio) > 1900
    except ValueError:
        return False
def validar_ranking(ranking):
    try:
        val=int(ranking)
        return 1<=val<=5
    except ValueError:
        return False
def regristrar_nuevo_auto(id_auto, marca, modelo, anio, ranking, fecha_ingreso, fecha_venta):
    if id_auto in autos or id_auto in operaciones:
        print("Error: El ID ya esta registrado.")
        return False
    if not validar_texto(id_auto) or not validar_texto(marca) or not validar_texto(modelo) or not validar_texto(anio) or not validar_texto(ranking) or not validar_texto(fecha_ingreso) or not validar_texto(fecha_venta):
        print("Error: Los cammpos de texto no pueden estar vacios ni contener solo espacios.")
        return False
    if not validar_anio(anio):
        print("Error: El año debe ser un numero mayor a 1900.")
        return False 
    if not validar_ranking(ranking):
        print("Error: El ranking debe ser un numero entero entre 1 y 5.")
        return False
    
    autos[id_auto]=[marca.strip(), modelo.strip(), int(anio), int(ranking)]
    operaciones[id_auto]=[fecha_ingresada.strip(), fecha_venta.strip()]
    print("Auto registrado con exito en el catalogo.")
    return True

def eliminar_auto(id_auto):
    if id_auto in autos and id_auto in operaciones:
        del autos[id_auto]
        del operaciones[id_auto]
        return True
    else:
        return False
    
id_a_borrar= input("Ingrese el ID del auto que desea dar de baja: ").upper()
if eliminar_auto(id_a_borrar):
    print(f"El vehicuulo con ID {id_a_borrar} ha sido eliminado del sistema de forma concurrente.")
else:
    print("Fallo en la operacion: El identificadoor no se encuentra registrado en el sistema")
