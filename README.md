# Advent of Code - 2022

## Day 1: Calorie counting

[instructions](https://adventofcode.com/2022/day/1)

### Part One

From a naive perspective today's problem could be solved with a one liner such as : 
```python
max([ sum([int(y) for y in x.split("\n")]) for x in open("./input").read().split("\n\n")[:-1] ])
```
But my goal is to aim for a balanced solution between performance and readability.

My solution is pretty straightforward:
```python
def calorie_counting():
    buffer, max_calorie = 0, 0
    with open("./input") as file:
        for line in file:
            if line == "\n":
                max_calorie = max(max_calorie, buffer)
                buffer = 0
            else:
                buffer += int(line.rstrip("\n"))
    return buffer if buffer > max_calorie else max_calorie
``` 
Since the file is being read line by line memory consumption is minimal and we only need 2 variables to store values between loop:
- `buffer` to store the total amount of calories held by a single Elf
- `max_calorie` to store the maximum amount held by one of the Elf

### Part Two

The second part isn't much more challenging; the only basic optimisation I can see is to not store all the values in a list and get the top 3 at the end but instead to use a stack to minimize memory consumption. In theory there is no limit in number of Elves to count from.

```python
import collections


def calorie_counting_top_n(top_n=3):
    buffer = 0
    max_calorie = collections.deque([0] * top_n, top_n)

    def stack_insert(buffer):
        if buffer > max_calorie[0]:
            max_calorie.popleft()
            index = 0
            while index < top_n - 1:
                if max_calorie[index] < buffer:
                    index += 1
                else:
                    break
            max_calorie.insert(index, buffer)
        return max_calorie

    with open("./input") as file:
        for line in file:
            if line == "\n":
                stack_insert(buffer)
                buffer = 0
            else:
                buffer += int(line.rstrip("\n"))
    return sum(stack_insert(buffer))
``` 

## Day 2: Rock Paper Scissors

[instructions](https://adventofcode.com/2022/day/2)

### Part One

My first thought was to use map in order to be able to match the adversary play to mine, but it is also possible to use the integer representation of the letters:
```python
def play(a, b):
    a = ord(a) - 64
    b = ord(b) - 87
    if a == b:
        return 3 + b
    elif ((b - a) != 2 and (a < b)) or (a - b == 2):
        return 6 + b
    return b


def rps_strategy():
    score = 0
    with open("./input") as file:
        for line in file:
            score += play(*line.rstrip("\n").split(" "))
    return score
```

The `play` function compare both players hand and return either `3` plus the hand value if it's a tie, `6` plus the hand value if we're winning and just the hand value if we are losing. 

### Part Two

Exactly the same as before except we need to change the value returned depending on the adversary hand:
```python
def play(a, b):
    a = ord(a) - 64
    b = ord(b) - 87
    if b == 1:
        return (3 * (a == 1)) + (a - 1)
    elif b == 2:
        return 3 + a
    return 6 + (a % 3) + 1


def rps_strategy():
    score = 0
    with open("./input") as file:
        for line in file:
            score += play(*line.rstrip("\n").split(" "))
    return score
```

## Day 3: Rucksack Reorganization

[instructions](https://adventofcode.com/2022/day/3)

### Part One

This problem is a classical intersection between 2 lists problem:
```python
def item_management(item_list):
    duplicate = ord(
        (
            set(item_list[: len(item_list) // 2])
            & set(item_list[len(item_list) // 2 :])
        ).pop()
    )
    if duplicate >= 97:
        return duplicate - 96
    else:
        return duplicate - 38


def rucksack_reorganization():
    score = 0
    with open("./input") as file:
        for line in file:
            score += item_management(line.rstrip("\n"))
    return score
```

The `item_management` function may need a bit of explanation:
- first the duplicate variable takes the `item_list` and split it, creating two [Python set](https://docs.python.org/3/tutorial/datastructures.html#sets). The use of the `&` operator create an intersection between both sets, giving us the only item present in both. Finally we use `ord` to get the numerical value of the item
- in a second time we convert the numerical value of the item to the priority order given in the instruction. The unicode value for `a` being higher than the one of `A`, we need to have a basic condition in order to know which number to substract.

Complexity of the code is `O(m+n)` and I really don't see any possible major optimisation.

### Part Two

Second part was really simple following the code I used previously:
```python
def group_identification(a, b, c):
    char = ord((set(a) & set(b) & set(c)).pop())
    if char >= 97:
        return char - 96
    else:
        return char - 38


def rucksack_reorganization():
    score = 0
    group = []
    with open("./input") as file:
        for line in file:
            group.append(line.rstrip("\n"))
            if len(group) == 3:
                score += group_identification(*group)
                group.clear()
    return score
```
I could technically read the input lines 3 by 3 instead of storing them in an array but I'm too lazy for that.

## Day 4: Camp Cleanup

[instructions](https://adventofcode.com/2022/day/4)

### Part One

This first part had me hesitating a bit about the code I should produce in order to maximize reusability for today's Part Two.

After some hesitation I went for the simplest code I could think of:
```python
def pair_inclusion(a, b):
    a = [int(x) for x in a.split("-")]
    b = [int(x) for x in b.split("-")]
    if (a[0] <= b[0] and a[1] >= b[1]) or (b[0] <= a[0] and b[1] >= a[1]):
        return 1
    return 0


def camp_cleanup():
    score = 0
    with open("./input") as file:
        for line in file:
            score += pair_inclusion(*line.rstrip("\n").split(","))
    return score
```

Not much magic here, I manually compare lower and higher bounds for the pairs in a line.

### Part Two

Second part was even easier, we only need to find if pairs are at least overlapping:
```python
def pair_inclusion(a, b):
    a = [int(x) for x in a.split("-")]
    b = [int(x) for x in b.split("-")]
    if (a[0] <= b[0] and a[1] >= b[0]) or (b[0] <= a[0] and b[1] >= a[0]):
        return 1
    return 0


def camp_cleanup():
    score = 0
    with open("./input") as file:
        for line in file:
            score += pair_inclusion(*line.rstrip("\n").split(","))
    return score
```


## Day 5: Supply Stacks

[instructions](https://adventofcode.com/2022/day/5)

### Part One

Today's challenge was pretty fun! The goal was to move around stack of crates while getting track of which crate went where.

I used some simple code and (again) a `deque` in order to use as less memory as possible:
```python
import collections
import re

def move_crates(stacks, crates, from_stack, to_stack):
    for index in range(crates):
        stacks[to_stack].append(stacks[from_stack].pop())


def fill_stack(stacks, line):
    for index in range(0, len(line)):
        if index + 1 not in stacks:
            stacks[index + 1] = collections.deque()
        if line[index].isalpha():
            stacks[index + 1].appendleft(line[index])


def supply_stacks():
    stacks = {}
    parse_stacks = True
    with open("./input") as file:
        for line in file:
            if parse_stacks:
                if line == "\n":
                    parse_stacks = False
                else:
                    fill_stack(stacks, line[1::4])
            else:
                move_crates(stacks, *map(int, re.findall("([\d]+)", line)))
    return "".join([stack.pop() for stack in stacks.values()])
```
The code is a bit messy so here are some explanations:
- when reading the input lines in the `supply_stack` function I first parse the crates stacks and store them in `stacks`, a `dict` of `deques`. Using `deques` allow to insert items at index `0` without much memory consumption
- once all lines describing the crates have been read, we go to the moving crates around part. The `move_crates` function simply use `deque` properties to remove the top crate in a pile and add it a the top of another pile

### Part Two

Interestingly, using `deque` in the fist part makes things more complex in the second part, since we need to move multiple crates at once, keeping their original order and `deque` can't `pop` multiple entries at once.

The code is almost the same as for the first part, except that we need a temporary buffer to hold the crates in their right order:
```python
import collections
import re

def move_crates(stacks, crates, from_stack, to_stack):
    crane_crates = collections.deque(
        [stacks[from_stack].pop() for index in range(crates)]
    )
    for index in range(crates):
        stacks[to_stack].append(crane_crates.pop())


def fill_stack(stacks, line):
    for index in range(0, len(line)):
        if index + 1 not in stacks:
            stacks[index + 1] = collections.deque()
        if line[index].isalpha():
            stacks[index + 1].appendleft(line[index])


def supply_stacks():
    stacks = {}
    parse_stacks = True
    with open("./input") as file:
        for line in file:
            if parse_stacks:
                if line == "\n":
                    parse_stacks = False
                else:
                    fill_stack(stacks, line[1::4])
            else:
                move_crates(stacks, *map(int, re.findall("([\d]+)", line)))
    return "".join([stack.pop() for stack in stacks.values()])
```

## Day 6: Tuning Trouble

[instructions](https://adventofcode.com/2022/day/6)

### Part One

Today's problem is really basic, we only need to be sure that all characters in a subarray are different:
```python
def tuning_trouble(signal_length):
    with open("./input") as file:
        line = file.read()
        for index in range(len(line) - signal_length):
            if len(set(line[index : index + signal_length])) == signal_length:
                return index + signal_length
```

It could technically be possible to optimize the search by skipping some index if we know that they are going to contains the same char (for example if we have `abcc` at index `0` we know that we could skip to index `3`) but I'm way too lazy to implement that functionnality.

### Part Two

Same as previous part except we need to call the function with `signal_length = 14`.


## Day 7: No Space Left On Device

[instructions](https://adventofcode.com/2022/day/7)

### Part One

I think that a lot of people will find that today's problem is way harder than Day 6 even if the guideline is obvious and the input file easy to parse. The main problem here is to find the right data structure to solve the problem.

At first I thought of using a recursive function, however since we need to read each line one after the other, using a simple loop was easier.

Here's my code:
```python
import collections
import re


def scan_device(max_size=100000):
    total_size = 0
    depth_size = collections.deque()
    with open("./input") as file:
        for line in file:
            if re.match("^\$ cd \.\.", line):
                buffer = depth_size.pop()
                if buffer <= max_size:
                    total_size += buffer
                depth_size[-1] += buffer
            elif re.match("^\$ cd", line):
                depth_size.append(0)
            elif re.match("([\d]+)", line):
                depth_size[-1] += int(re.match("([\d]+)", line)[0])

        for depth in depth_size:
            if depth <= max_size:
                total_size += depth
            else:
                break

        if sum(depth_size) <= max_size:
            total_size += sum(depth_size)
        return total_size
```

### Part Two

The second part is kind of the same as the first one, except that we need to store the size of each folder and find the right candidate:
```python
import collections
import re


def scan_device():
    occupied_space = 0
    total_disk_size = 70000000
    required_disk_space = 30000000
    deletion_candidate = 70000000
    directories_size = []

    depth_size = collections.deque()
    with open("./input") as file:
        for line in file:
            if re.match("^\$ cd \.\.", line):
                buffer = depth_size.pop()
                depth_size[-1] += buffer
                directories_size.append(buffer)
            elif re.match("^\$ cd", line):
                depth_size.append(0)
            elif re.match("([\d]+)", line):
                depth_size[-1] += int(re.match("([\d]+)", line)[0])
                occupied_space += int(re.match("([\d]+)", line)[0])

        depth_size.reverse()
        buffer = 0
        for depth in depth_size:
            buffer += depth
            directories_size.append(buffer)

        minimal_required_space = required_disk_space - (
            total_disk_size - occupied_space
        )
        for directory_size in directories_size:
            if (
                directory_size >= minimal_required_space
                and directory_size < deletion_candidate
            ):
                deletion_candidate = directory_size
        return deletion_candidate
```

## Day 8: Treetop Tree House

[instructions](https://adventofcode.com/2022/day/8)

### Part One

Today's problem wasn't much of a challenge as long as I didn't cared about performance and complexity.

My code for the first part is really verbose:
```
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


### Part Two

Second part of today's problem was easier to write in a more compact way:
```
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


## Day 9: Rope Bridge

[instructions](https://adventofcode.com/2022/day/9)

### Part One

Today's problem doesn't require a lot of coding skill but some basic logical understanding. Both a notebook and a visualization function can be of great help to find the solution.

Here's my code for the first part:
```python
def rope_bridge():
    tail_x,tail_y,head_x,head_y = 0,0,0,0
    with open("./input") as file:
        covered_cells = {"0_0": 1}
        for line in file:
            direction, movements = line.rstrip().split(" ")
            if direction == "R":
                head_x = head_x + int(movements)
            elif direction == "L":
                head_x = head_x - int(movements)
            elif direction == "U":
                head_y = head_y + int(movements)
            elif direction == "D":
                head_y = head_y - int(movements)

            while (
                (abs(head_x - tail_x) + abs(head_y - tail_y)) / 2 > 1
                or abs(head_x - tail_x) > 1
                or abs(head_y - tail_y) > 1
            ):
                if head_x - tail_x > 0:
                    tail_x += 1
                elif head_x - tail_x < 0:
                    tail_x += -1
                if head_y - tail_y > 0:
                    tail_y += 1
                elif head_y - tail_y < 0:
                    tail_y += -1

                covered_cells[f"{tail_x}_{tail_y}"] = True
                
        return sum([visited_count for visited_count in covered_cells.values()])
```
Basically we read the file line by line and move the "head" instantly from one point to another. Then, we move the tail using the shortest path (either in diagonal or in a straight line/column), always keeping to the tile previously occupied by the tail. I used a dictionnary (`covered_cells`) as a way to keep track of every visited cells.

### Part Two

As I expected my code isn't reusable from scratch. The main problem here is that each knot on the rope can move in a different direction and will try to move in the shortest way possible relatively to the previous knot. However, the whole rope doesn't move in a straight line.

Here's my code:
```python
def rope_bridge(rope_size=9):
    head_x,head_y = 0,0
    rope_knots = []
    for knot in range(rope_size):
        rope_knots.append({"x": 0, "y": 0})
    covered_cells = {"0_0": True}
    with open("./input") as file:    
        for line in file:
            direction,movements = line.rstrip().split(" ")
            target_x,target_y = head_x,head_y
            if(direction == "R"):
                target_x = head_x+int(movements)
            elif(direction == "L"):
                target_x = head_x-int(movements)
            elif(direction == "U"):
                target_y = head_y+int(movements)
            elif(direction == "D"):
                target_y = head_y-int(movements)

            while(head_x != target_x or head_y != target_y):
                if(head_x < target_x):
                    head_x += 1
                elif(head_x > target_x):
                    head_x -= 1
                if(head_y < target_y):
                    head_y += 1
                elif(head_y > target_y):
                    head_y -= 1

                for index,knot in enumerate(rope_knots):
                    if(index == 0):
                        knot_head_x = head_x
                        knot_head_y = head_y
                    else:
                        knot_head_x = rope_knots[index-1]["x"]
                        knot_head_y = rope_knots[index-1]["y"]
                    while(
                        (abs(knot_head_x - knot["x"]) + abs(knot_head_y - knot["y"]))/2 > 1
                        or abs(knot_head_x - knot["x"]) > 1
                        or abs(knot_head_y - knot["y"]) > 1
                        ):
                        if(knot_head_x - knot["x"] > 0):
                            knot["x"] += 1
                        elif(knot_head_x - knot["x"] < 0):
                            knot["x"] += -1
                        if(knot_head_y - knot["y"] > 0):
                            knot["y"] += 1
                        elif(knot_head_y - knot["y"] < 0):
                            knot["y"] += -1
                        if(index == rope_size-1):
                            covered_cells[f"{knot['x']}_{knot['y']}"] = True

        return sum([visited_count for visited_count in covered_cells.values()])
```
The main change here is that each time the head move, we need to calculate its position one tile at time in order to update the position of the knots correctly. Also, each knot position is computed relatively to the previous knot.