"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """ 
    
    file = open("data.csv", "r")
    suma = 0 
    
    for renglon in file:
        suma += int((renglon.split())[1])
    
    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    file = open("data.csv", "r")
    registros = {}
    
    for renglon in file:
        renglon = renglon.split()
        if renglon[0] in registros:
            registros[renglon[0]] += 1
        else: 
            registros[renglon[0]] = 1
            
    return sorted(registros.items(), key= lambda x: x[0])


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    file = open("data.csv", "r")
    registros = {}
    
    for renglon in file:
        renglon = renglon.split()
        if renglon[0] in registros:
            registros[renglon[0]] += int(renglon[1])
        else: 
            registros[renglon[0]] = int(renglon[1])
            
    return sorted(registros.items(), key= lambda x: x[0])


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    file = open("data.csv", "r")
    registros = {}
    
    for renglon in file:
        renglon = renglon.split()
        mes = (renglon[2].split("-"))[1]
        if mes in registros:
            registros[mes] += 1
        else:
            registros[mes] = 1
    
    return sorted(registros.items(), key= lambda x: x[0])


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    
    file = open("data.csv", "r")
    registros = []
    
    for renglon in file:
        renglon = renglon.split()
        esta = False
        
        for dir in registros:
            if dir["letra"] == renglon[0]:
                esta = True
                break
        
        if not esta:
            registros.append({
                "letra":renglon[0],
                "max":int(renglon[1]),
                "min":int(renglon[1])
            })
        else:
            for dir in registros:
                if dir["letra"] == renglon[0]:
                    if dir["max"] < int(renglon[1]):
                        dir["max"] = int(renglon[1])
                        
                    elif dir["min"] > int(renglon[1]):
                        dir["min"] = int(renglon[1])
    
    registros_final = []
    for dir in registros:
        registros_final.append((dir["letra"],dir["max"],dir["min"],))
        
    return sorted(registros_final, key=lambda x: x[0])


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    
    file = open("data.csv", "r")
    registros = []
    
    for renglon in file:
        diccionarios = renglon.split()[4]
        diccionarios = diccionarios.split(',')
 
        for d in diccionarios:
            key , ele = d.split(':')
            ele = int(ele)
            exist = False
            
            for dir in registros:
                if dir["clave"] == key:
                    
                    if dir["min"] > ele:
                        dir["min"] = ele
                    if dir["max"] < ele:
                        dir["max"] = ele
                        
                    exist = True
                
            if not exist:
                registros.append({
                    "clave":key,
                    "min":ele,
                    "max":ele
                })
    
    registros = [(r["clave"],r["min"],r["max"]) for r in registros]
    
    return sorted(registros, key= lambda x: x[0])


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    
    file = open("data.csv", "r")
    registros = []
    
    for renglon in file:
        letra, num = renglon.split()[0:2]
        num = int(num)
        exist = False
        
        for dir in registros:
            if dir["num"] == num:
                dir["letras"].append(letra)
                exist = True
            
        if not exist:
            registros.append({
                "num":num,
                "letras":[letra]
            })
    
    registros = [(r["num"],r["letras"]) for r in registros]
    
    return sorted(registros, key= lambda x: x[0])


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    file = open("data.csv", "r")
    registros = []
    
    for renglon in file:
        letra, num = renglon.split()[0:2]
        num = int(num)
        exist = False
        
        for dir in registros:
            if dir["num"] == num:
                if letra not in dir["letras"]:
                    dir["letras"].append(letra)
                exist = True
            
        if not exist:
            registros.append({
                "num":num,
                "letras":[letra]
            })
    
    registros = [(r["num"],sorted(r["letras"])) for r in registros]
    
    return sorted(registros, key= lambda x: x[0])


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    
    file = open("data.csv","r")
    registros = {}
    
    for renglon in file:
        keys = renglon.split()[4]
        keys = keys.split(',')
        keys = [k.split(":")[0] for k in keys]
        
        for key in keys:
            if key not in registros.keys():
                registros[key] = 1
            else:
                registros[key] += 1
    
    registros_ord = {}
    
    for clave in sorted(registros):
        registros_ord[clave] = registros[clave]
        
    return registros_ord


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return
