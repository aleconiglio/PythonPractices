import random

choice = ["piedra", "papel", "tijera"]
boss = random.choice(choice)
player = None
again = "si"

while again == "si":
    player = input("Piedra, papel o tijera?🤔: ").lower()
    while player not in choice:
        player = input("Escribí bien 🤬 Piedra, papel o tijera? : ").lower()
    if player == boss:
       print("Bot 🤖-> ", boss)
       print("_______EMPATE 😐_______")
    elif boss == "piedra" and player == "tijera":
       print("Bot 🤖-> ", boss)
       print("_______PERDISTE 😞_______")
    elif boss == "piedra" and player == "papel":
       print("Bot 🤖-> ", boss)
       print("_______GANASTE 🥳_______")
    elif boss == "papel" and player == "piedra":
       print("Bot 🤖-> ", boss)
       print("_______PERDISTE 😞_______")
    elif boss == "papel" and player == "tijera":
       print("Bot 🤖-> ", boss)
       print("_______GANASTE 🥳_______")
    elif boss == "tijera" and player == "papel":
       print("Bot 🤖-> ", boss)
       print("_______PERDISTE 😞_______")
    elif boss == "tijera" and player == "piedra":
       print("Bot 🤖-> ", boss)
       print("_______GANASTE 🥳_______")
    again = input("'si' para jugar otra vez y 'no' para no jugar mas: ").lower()
