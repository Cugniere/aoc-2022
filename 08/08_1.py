def treetop_tree_house():
    with open("./input") as file:
        tree_lines = [
            [int(value) for value in list(line)]
            for line in file.read().split("\n")[:-1]
        ]
        size = len(tree_lines)
        highest_tree = {
            "top": [-1] * size,
            "bottom": [-1] * size,
            "left": [-1] * size,
            "right": [-1] * size,
        }
        visible_trees = [[0] * size for i in range(size)]

        for y, line in enumerate(tree_lines):
            for x, value in enumerate(line):
                r_x = size - 1 - x
                r_y = size - 1 - y
                if value > highest_tree["top"][x]:
                    visible_trees[y][x] = 1
                    highest_tree["top"][x] = max(value, highest_tree["top"][x])
                if value > highest_tree["left"][y]:
                    visible_trees[y][x] = 1
                    highest_tree["left"][y] = max(value, highest_tree["left"][y])

        for y, line in enumerate(tree_lines[::-1]):
            for x, value in enumerate(line[::-1]):
                r_x = size - 1 - x
                r_y = size - 1 - y
                if value > highest_tree["bottom"][r_x]:
                    visible_trees[r_y][r_x] = 1
                    highest_tree["bottom"][r_x] = max(
                        value, highest_tree["bottom"][r_x]
                    )
                if value > highest_tree["right"][r_y]:
                    visible_trees[r_y][r_x] = 1
                    highest_tree["right"][r_y] = max(value, highest_tree["right"][r_y])

        return sum([sum(row) for row in visible_trees])


print(treetop_tree_house())
