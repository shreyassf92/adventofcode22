import collections
import re


def get_starting_stacks_formation():
    stacks = []
    for i in range(stacks_count + 1):
        stacks.append(collections.deque())

    with open("./5/input-stacks.txt") as input:
        input = input.read().splitlines()
        for line in input:
            for i in range(0, len(line), 4):
                crate = line[i : i + 4].strip()
                if crate != "":
                    stacks[(i // 4) + 1].append(crate)
    return stacks


stacks_count = 9  # read it from file

# part 1
stacks = get_starting_stacks_formation()
with open("./5/input-operations.txt") as input:
    for op in input.read().splitlines():
        num_of_stacks_to_move, frm, to = map(lambda x: int(x), re.findall(r"\d+", op))
        for i in range(num_of_stacks_to_move):
            stacks[to].appendleft(stacks[frm].popleft())  
    
    print("".join([stack[0] for stack in stacks if len(stack) > 0]))

# part 2
stacks = get_starting_stacks_formation()
with open("./5/input-operations.txt") as input:
    for op in input.read().splitlines():
        num_of_stacks_to_move, frm, to = map(lambda x: int(x), re.findall(r"\d+", op))
        for i in range(num_of_stacks_to_move-1, -1, -1):
            stacks[to].appendleft(stacks[frm][i])
        for i in range(num_of_stacks_to_move):
            stacks[frm].popleft()

    print("".join([stack[0] for stack in stacks if len(stack) > 0]))

