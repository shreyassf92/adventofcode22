

DRAW = 3
WIN = 6

POINTS_MAP = {
    "X" : 1,
    "Y": 2,
    "Z": 3,
}

def get_my_points_for_the_round(round : str):
    opponent_choice, my_choice = round.strip().split(" ")
    
    # my win conditions
    if (my_choice == "X" and opponent_choice == "C") or (my_choice == "Y" and opponent_choice == "A") or (my_choice == "Z" and opponent_choice == "B"):
        return WIN + POINTS_MAP.get(my_choice)
    # my loss condition
    elif (my_choice == "X" and opponent_choice == "B") or (my_choice == "Y" and opponent_choice == "C") or (my_choice == "Z" and opponent_choice == "A"):
        return POINTS_MAP.get(my_choice)
    #draw
    return DRAW + POINTS_MAP.get(my_choice)


my_points = 0

with open("./2/input.txt") as input:
    for round in input:
        my_points += get_my_points_for_the_round(round)

    print(my_points)