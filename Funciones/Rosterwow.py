personajes = {
    'P01': ['Thrall', 'Chamán', 80, 2500],    # [Nombre, Clase, Nivel, Daño por segundo (DPS)]
    'P02': ['Jaina', 'Mago', 80, 3100],
    'P03': ['Arthas', 'Paladín', 75, 1800],
    'P04': ['Sylvanas', 'Cazador', 80, 2900],
    'P05': ['Illidan', 'Cazador de Demonios', 78, 2200]
}

estado_raid = {
    'P01': ['Listo', 'Tanque'],               # [Estado de conexión, Rol en el grupo]
    'P02': ['Listo', 'DPS'],
    'P03': ['Desconectado', 'Tanque'],
    'P04': ['Listo', 'DPS'],
    'P05': ['Desconectado', 'DPS']
}


def filtrar_listos_por_clase(clase_buscada):
    encontrado = False  
    
    for id, datos in personajes.items():
        if clase_buscada == datos[1] and estado_raid[id][0] == "Listo":
            print(f"{datos[0]} -- Rol: {estado_raid[id][1]} (DPS: {datos[3]})")
            encontrado = True
            
    if encontrado == False:
        print("No hay jugadores listos de esa clase.")