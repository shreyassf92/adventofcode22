with open("./4/input.txt") as input:
    pairs = input.read().splitlines()
    full_overlapping_pair_count = 0
    any_overlapping_pair_count = 0

    for pair in pairs:
        range1, range2 = [
            tuple(map(lambda x: int(x), range.split("-"))) for range in pair.split(",")
        ]

        tmp = ()
        if range1[1] - range1[0] < range2[1] - range2[0]:
            tmp = range1
            range1 = range2
            range2 = tmp

        # part 1
        if range2[0] >= range1[0] and range2[1] <= range1[1]:
            full_overlapping_pair_count += 1

        # part 2
        if range1[0] <= range2[0] <= range1[1] or range1[0] <= range2[1] <= range1[1]:
            any_overlapping_pair_count += 1

    print(full_overlapping_pair_count)
    print(any_overlapping_pair_count)
