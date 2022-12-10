grid = []
no_tree_visible = 0

with open("./8/input_sample.txt") as input:
    for line in input.read().splitlines():
        grid.append(line)

# part 1
no_tree_visible = len(grid) * 2 + (len(grid[0]) - 2) * 2

for i in range(1, len(grid[0]) - 1):
    for j in range(1, len(grid) - 1):
        curr_tree_len = int(grid[j][i])

        # top
        tree_visible = True
        for t in range(j - 1, -1, -1):
            if int(grid[t][i]) >= curr_tree_len:
                tree_visible = False
                break

        # bottom
        if not tree_visible:
            tree_visible = True
            for b in range(j + 1, len(grid)):
                if int(grid[b][i]) >= curr_tree_len:
                    tree_visible = False
                    break

        # left
        if not tree_visible:
            tree_visible = True
            for l in range(i - 1, -1, -1):
                if int(grid[j][l]) >= curr_tree_len:
                    tree_visible = False
                    break

        # right
        if not tree_visible:
            tree_visible = True
            for r in range(i + 1, len(grid[0])):
                if int(grid[j][r]) >= curr_tree_len:
                    tree_visible = False
                    break

        if tree_visible:
            no_tree_visible += 1

print(no_tree_visible)


# part 2
highest_scenic_score = 0

for i in range(0, len(grid[0])):
    for j in range(0, len(grid)):
        curr_tree_len = int(grid[j][i])

        # top
        top_score = 0
        neighbor_len = curr_tree_len
        for t in range(j - 1, -1, -1):
            local_len = int(grid[t][i])
            if abs(j - t) == 1:  # imediate neighbor
                top_score += 1
                neighbor_len = local_len
            elif local_len >= neighbor_len:
                top_score += 1
                neighbor_len = local_len
                if local_len >= curr_tree_len:
                    break
            else:
                break

        # bottom
        bottom_score = 0
        neighbor_len = curr_tree_len
        for b in range(j + 1, len(grid)):
            local_len = int(grid[b][i])
            if abs(j - b) == 1:  # imediate neighbor
                bottom_score += 1
                neighbor_len = local_len
            elif local_len >= neighbor_len:
                bottom_score += 1
                neighbor_len = local_len
                if local_len >= curr_tree_len:
                    break
            else:
                break

        # left
        left_score = 0
        neighbor_len = curr_tree_len
        for l in range(i - 1, -1, -1):
            local_len = int(grid[j][l])
            if abs(i - l) == 1:  # imediate neighbor
                left_score += 1
                neighbor_len = local_len
            elif local_len >= neighbor_len:
                left_score += 1
                neighbor_len = local_len
                if local_len >= curr_tree_len:
                    break
            else:
                break

        # right
        right_score = 0
        neighbor_len = curr_tree_len
        for r in range(i + 1, len(grid[0])):
            local_len = int(grid[j][r])
            if abs(i - r) == 1:  # imediate neighbor
                right_score += 1
                neighbor_len = local_len
            elif local_len >= neighbor_len:
                right_score += 1
                neighbor_len = local_len
                if local_len >= curr_tree_len:
                    break
            else:
                break

        score = top_score * bottom_score * left_score * right_score
        highest_scenic_score = max(highest_scenic_score, score)

print(highest_scenic_score)
