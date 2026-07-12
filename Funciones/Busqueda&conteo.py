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

def contar_vendidos_por_anio(anio_buscado):
    total_vendidos=0
    for id, datos in autos.items():
        if anio_buscado==datos[2] and operaciones[id][1]!="Pendiente":
            total_vendidos+=1
    print(f"Total de autos vendidos del año {anio_buscado}: {total_vendidos}")

Menu="""
---- MENU ----
1.Autos vendidos por año
"""

while True:
    print(Menu)
    op=int(input("Ingrese la opcion: "))
    match op:
        case 1:
            anio_buscado=int(input("Ingrese el año a buscar: "))
            contar_vendidos_por_anio(anio_buscado)