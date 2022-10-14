#detectar si existe el file //////////////////
import os

path = "C:/Users/lolo_/PycharmProjects/ejercicios"

if os.path.exists(path):
    print("Path does exists")
    if os.path.isdir(path):
        print("And it is a folder")
    else:
        print("But is not a folder")
else:
    print("Path doesn't exists")

#leer file /////////////////////////////

with open("FILE") as file:
    print(file.read())

"""
para que no te tire el error en caso de que no exista, se puede hacer un try:

try:
    with open("FILE") as file:
        print(file.read())
except blablabla:
    print()
"""
#escribir en file//////////////////////////////////

text = "holaaaa\n whats up\n bro"
with open("FILE", "w") as file:
    file.write(text)
# en el segundo parametro puede ir "w" para sobreescribir y "a" para agregar