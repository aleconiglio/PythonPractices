import json
import pickle

datos = {}
datos["equipo"] = []

alejo = {"id": 1001, "nombre": "Alejo", "numero": 7, "posicion": "delantero", "goles": 5}
carlos = {"id": 1002, "nombre": "Carlos", "numero": 9, "posicion": "delantero", "goles": 6}
jorge = {"id": 1003, "nombre": "Jorge", "numero": 3, "posicion": "defensor", "goles": 2}
roberto = {"id": 1004, "nombre": "Roberto", "numero": 1, "posicion": "arquero", "goles": 0}

datos["equipo"].append(alejo)
datos["equipo"].append(carlos)
datos["equipo"].append(jorge)
datos["equipo"].append(roberto)

#pasar los datos a un json:
with open("C:/Users/lolo_/PycharmProjects/ejercicios/equipo.json", "w") as f:
    json.dump(datos, f)

#leer datos de un json:
with open("C:/Users/lolo_/PycharmProjects/ejercicios/equipo.json", "r") as f:
    datos_equipo = json.load(f)

for e in datos_equipo["equipo"]:
    print("ID:",  e["id"])
    print("Nombre:",  e["nombre"])
    print("Numero:",  e["numero"])
    print("Posicion:",  e["posicion"])
    print("Goles:",  e["goles"])
    print("")