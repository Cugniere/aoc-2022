def tree_view(height, tree_group):
    for view, tree in enumerate(tree_group):
        if tree >= height:
            return view + 1
    return len(tree_group)


def scenic_tree():
    with open("./input") as file:
        tree_lines = [
            [int(value) for value in list(line)]
            for line in file.read().split("\n")[:-1]
        ]
        size = len(tree_lines)
        max_scenic_score = 0

        for y in range(1, size - 1):
            for x in range(1, size - 1):
                left_view = tree_view(tree_lines[y][x], tree_lines[y][x - 1 :: -1])
                right_view = tree_view(tree_lines[y][x], tree_lines[y][x + 1 :])
                top_view = tree_view(
                    tree_lines[y][x], [tree_lines[n][x] for n in range(0, y)][::-1]
                )
                bottom_view = tree_view(
                    tree_lines[y][x], [tree_lines[n][x] for n in range(y + 1, size)]
                )
                max_scenic_score = max(
                    max_scenic_score, left_view * right_view * top_view * bottom_view
                )

        return max_scenic_score


print(scenic_tree())
