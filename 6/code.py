datastream = ""
with open("./6/input.txt") as input:
    datastream = input.read()

# part 1
char_map = {}
start_index, end_index = 0, 0
for end_index in range(len(datastream)):
    ch = datastream[end_index]
    if ch in char_map.keys():
        start_index = char_map[ch] + 1

    char_map[ch] = end_index

    for k in list(char_map.keys()):
        if char_map[k] < start_index:
            char_map.pop(k)

    if end_index - start_index == 3:  # found 4 chars
        break

print(end_index + 1)  # adding +1 to offset 0 index

# part 2
char_map = {}
start_index, end_index = 0, 0
for end_index in range(len(datastream)):
    ch = datastream[end_index]
    if ch in char_map.keys():
        start_index = char_map[ch] + 1

    char_map[ch] = end_index

    for k in list(char_map.keys()):
        if char_map[k] < start_index:
            char_map.pop(k)

    if end_index - start_index == 13:  # found 4 chars
        break

print(end_index + 1)  # adding +1 to offset 0 index
