DRAW = 3
WIN = 6

CHOICE_INDEX = {"A": 0, "B": 1, "C": 2}

CHOICE_INDEX_REV = {0: "A", 1: "B", 2: "C"}

POINTS_MAP = {
    "A": 1,
    "B": 2,
    "C": 3,
}


def get_my_points_for_the_round(round: str):
    opponent_choice, result = round.strip().split(" ")
    opp_index = 0
    my_choice = ""

    # lose
    if result == "X":
        opp_choice_index = CHOICE_INDEX.get(opponent_choice)
        my_choice = CHOICE_INDEX_REV.get((opp_choice_index + 2) % 3)
        return POINTS_MAP.get(my_choice)

    # draw
    elif result == "Y":
        return DRAW + POINTS_MAP.get(opponent_choice)

    # win
    else:
        opp_choice_index = CHOICE_INDEX.get(opponent_choice)
        my_choice = CHOICE_INDEX_REV.get((opp_choice_index + 1) % 3)
        return WIN + POINTS_MAP.get(my_choice)


my_points = 0

with open("./2/input.txt") as input:
    for round in input:
        my_points += get_my_points_for_the_round(round)

    print(my_points)
