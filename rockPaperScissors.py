import random

choice = ["piedra", "papel", "tijera"]
boss = random.choice(choice)
player = None
again = "si"

while again == "si":
    player = input("Piedra, papel o tijera?π€: ").lower()
    while player not in choice:
        player = input("EscribΓ­ bien π€¬ Piedra, papel o tijera? : ").lower()
    if player == boss:
       print("Bot π€-> ", boss)
       print("_______EMPATE π_______")
    elif boss == "piedra" and player == "tijera":
       print("Bot π€-> ", boss)
       print("_______PERDISTE π_______")
    elif boss == "piedra" and player == "papel":
       print("Bot π€-> ", boss)
       print("_______GANASTE π₯³_______")
    elif boss == "papel" and player == "piedra":
       print("Bot π€-> ", boss)
       print("_______PERDISTE π_______")
    elif boss == "papel" and player == "tijera":
       print("Bot π€-> ", boss)
       print("_______GANASTE π₯³_______")
    elif boss == "tijera" and player == "papel":
       print("Bot π€-> ", boss)
       print("_______PERDISTE π_______")
    elif boss == "tijera" and player == "piedra":
       print("Bot π€-> ", boss)
       print("_______GANASTE π₯³_______")
    again = input("'si' para jugar otra vez y 'no' para no jugar mas: ").lower()
