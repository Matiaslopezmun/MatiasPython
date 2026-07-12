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

def buscar_por_rango(anio_min, anio_max):
    encontrados=[]

    for id, datos in autos.items():
        if anio_min<datos[2]<=anio_max and operaciones[id][1]=="Pendiente":
            texto = f"{datos[0]} {datos[1]}--{id}"
            encontrados.append(texto)
            
    encontrados.sort()

    print(f"\n--- Autos disponibles entre {anio_min} y {anio_max} ---")
    if len(encontrados) > 0:
        for auto in encontrados:
            print(auto)
    else:
        print("No se encontraron vehículos en ese rango.")
            
           
buscar_por_rango(2015, 2025)