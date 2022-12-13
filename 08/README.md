# Day 8: Treetop Tree House

[instructions](https://adventofcode.com/2022/day/8)

## Part One

Today's problem wasn't much of a challenge as long as I didn't cared about performance and complexity.

My code for the first part is really verbose:
```python
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
```

Basically I need to make 2 loop in order to check their visibility, firstly by checking their visibility from left and top and secondly by checking their visibility from bottom and right.

Algorithmic complexity is `O^2` but I don't see a better way to do this.


## Part Two

Second part of today's problem was easier to write in a more compact way:
```python
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
```

One evident optimisation is to no compute the score of the trees located on the edge of the map, saving `4n-4` calculations. Complexity is still `O^2` though.
