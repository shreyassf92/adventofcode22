
import heapq

calories = []

with open("./1/input.txt") as input:
    elf_calories = 0

    for line in input:
        if line != "\n":
            elf_calories += int(line)
        else: # next elf
            heapq.heappush(calories, elf_calories)
            elf_calories = 0 

    max_calories = heapq.nlargest(1, calories)
    print(f"Maximum calories carried by an elf is  ({max_calories})")

    max_three_calories =  sum(heapq.nlargest(3, calories))
    print(f"Sum of top three calories is  ({max_three_calories})")