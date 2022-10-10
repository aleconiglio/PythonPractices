import json

name = input("What is your name?: ")
age = input("What is your age?: ")
fav_color = input("Favorite color: ")
height = input("What is your height: ")
weight = input("What is your weight: ")
shoe_size = input("What is your shoe size: ")
country = input("What is your nationality: ")
file = input("File name: ")
result = [{'Name': name, 'Age': age, "Favorite color": fav_color, "Height": height, "Weight": weight, "Shoe size": shoe_size, "Nationality": country}]

with open("C:/Users/lolo_/Desktop/{}.txt".format(file), "w") as f:
    json.dump(result, f)