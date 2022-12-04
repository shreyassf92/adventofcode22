with open("./3/input.txt") as input:

    rucksacks = input.read().splitlines()

    # part 1
    sum_priorities = 0
    for rucksack in rucksacks:
        first_compartment, second_compartment = set(
            rucksack[: len(rucksack) // 2]
        ), set(rucksack[len(rucksack) // 2 :])
        common_item: str = set.intersection(first_compartment, second_compartment).pop()

        sum_priorities += (
            (ord(common_item) - 96)
            if common_item.islower()
            else (ord(common_item) - 64 + 26)
        )

    print(sum_priorities)

    # part 2
    sum_badge_priorities = 0
    for i in range(0, len(rucksacks), 3):
        elf_one, elf_two, elf_three = [set(rs) for rs in rucksacks[i : i + 3]]
        common_item = set.intersection(
            elf_one, set.intersection(elf_two, elf_three)
        ).pop()

        sum_badge_priorities += (
            (ord(common_item) - 96)
            if common_item.islower()
            else (ord(common_item) - 64 + 26)
        )

    print(sum_badge_priorities)
