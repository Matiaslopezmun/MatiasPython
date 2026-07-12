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

def actualizar_ranking(id_auto, nuevo_ranking):
    if id_auto in autos:
        autos[id_auto][3]=nuevo_ranking
        return True
    else:
        return False
    

id_auto=input("Ingresa la id del auto: ").upper()
nuevo_ranking=int(input("Ingresa el nuevo ranking: "))
exito=actualizar_ranking(id_auto, nuevo_ranking)

if exito==True:
    print(f"¡Éxito! El nuevo ranking del vehículo con ID '{id_auto}' es de {nuevo_ranking}.")
else:
    print("Error: El ID ingresado no existe en el sistema.")





