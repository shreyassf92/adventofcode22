from math import sqrt, pow

DIRECTION = {
    "U": (0, 1),
    "D": (0, -1),
    "L": (-1, 0),
    "R": (1, 0),
    "UR": (1, 1),
    "UL": (-1, 1),
    "DL": (-1, -1),
    "DR": (1, -1),
}


def get_distance(head: tuple, tail: tuple) -> float:
    return sqrt(pow(tail[0] - head[0], 2) + pow(tail[1] - head[1], 2))


def get_tails_move(head: tuple, tail: tuple, head_direction: str) -> tuple:

    distance = get_distance(head, tail)

    # check if head and tail in same row or column
    if head[0] == tail[0] or head[1] == tail[1]:
        if distance > 1:
            return DIRECTION.get(head_direction)
    else:
        if distance > 1.42:
            # up - right
            if head[0] > tail[0] and head[1] > tail[1]:
                return DIRECTION.get("UR")
            # up - left
            elif head[0] < tail[0] and head[1] > tail[1]:
                return DIRECTION.get("UL")
            # down - left
            elif head[0] < tail[0] and head[1] < tail[1]:
                return DIRECTION.get("DL")
            # down - right
            elif head[0] > tail[0] and head[1] < tail[1]:
                return DIRECTION.get("DR")

    return (0, 0)


input = None
with open("./9/input.txt") as input:
    input = input.read().splitlines()

# part 1
tail_points = set()
head, tail = (0, 0), (0, 0)

tail_points.add(tail)
for motion in input:
    m_split = motion.split(" ")
    dir = m_split[0]
    steps = int(m_split[1])

    for step in range(1, steps + 1):
        head = tuple(map(sum, zip(head, DIRECTION.get(dir))))
        tails_next_move = get_tails_move(head, tail, dir)
        if tails_next_move != (0, 0):
            tail = tuple(map(sum, zip(tail, tails_next_move)))
            tail_points.add(tail)

print(len(tail_points))


# part 2
tail_points = set()
rope = []  # rope[0] is the head
for i in range(10):
    rope.append((0, 0))

tail_points.add(rope[9])
for motion in input:
    m_split = motion.split(" ")
    dir = m_split[0]
    steps = int(m_split[1])

    for step in range(1, steps + 1):
        rope[0] = tuple(map(sum, zip(rope[0], DIRECTION.get(dir))))

        for i in range(1, len(rope)):
            tails_next_move = get_tails_move(rope[i - 1], rope[i], dir)
            if tails_next_move != (0, 0):
                rope[i] = tuple(map(sum, zip(rope[i], tails_next_move)))
                if i == 9:
                    tail_points.add(rope[i])

print(len(tail_points))
