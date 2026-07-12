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

def validar_anio(anio):
    try:
        if int(anio) > 1900:
            return True
        else:
            print("Error: El año debe ser mayor a 1900.")
            return False
    except ValueError:
        print("Error: Debe ingresar estrictamente un número entero.")
        return False

def agregar_auto(id_auto, marca, modelo, anio, ranking, fecha_ingreso):
    if id_auto not in autos and validar_anio(anio) == True:
        autos[id_auto] = [marca, modelo, int(anio), int(ranking)]
        operaciones[id_auto] = [fecha_ingreso, "Pendiente"]
        print("¡Éxito! Vehículo registrado en el sistema.")
        return True  
    else:
        print("No se pudo registrar: El ID ya existe o el año es incorrecto.")
        return False