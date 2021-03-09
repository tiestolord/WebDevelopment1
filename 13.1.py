# HW 13.1

firstname = input("Enter Your firstname: ")
lastname = input("Enter Your lastname: ")
age = input("Enter Your age: ")
height = input("Enter Your height: ")
weight = input("Enter Your weight: ")
position = input("Enter Your position: ")



def make_player(firstname, lastname, age, height, weight, position):
    def description():
        return

    return {
        "firstname": firstname,
        "lastname": lastname,
        "age": age,
        "height": height,
        "weight": weight,
        "position": position,
    }

registered_player = make_player("firstname", "lastname", "age", "height", "weight", "position")

with open("football_players.txt", "w") as football_file:
    football_file.write(str(registered_player))

print("Your registered successfully.")
print(f"You are {firstname} {lastname}, your height is {height} & your weight is {weight}. Your best playing position is {position}.".format(registered_player))