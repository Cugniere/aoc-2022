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
                    fill_stack(
                        stacks,
                        [line[index : index + 1] for index in range(1, len(line), 4)],
                    )
            else:
                move_crates(
                    stacks, *[int(line.split(" ")[index]) for index in [1, 3, 5]]
                )
    return "".join([stacks[i + 1].pop() for i in range(len(stacks))])
```
The code is a bit messy so here are some explanations:
- when reading the input lines in the `supply_stack` function I first parse the crates stacks and store them in `stacks`, a `dict` of `deques`. Using `deques` allow to insert items at index `0` without much memory consumption
- once all lines describing the crates have been read, we go to the moving crates around part. The `move_crates` function simply use `deque` properties to remove the top crate in a pile and add it a the top of another pile

### Part Two

Interestingly, using `deque` in the fist part makes things more complex in the second part, since we need to move multiple crates at once, keeping their original order and `deque` can't `pop` multiple entries at once.

The code is almost the same as for the first part, except that we need a temporary buffer to hold the crates in their right order:
```python
import collections


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
                    fill_stack(
                        stacks,
                        [line[index : index + 1] for index in range(1, len(line), 4)],
                    )
            else:
                move_crates(
                    stacks, *[int(line.split(" ")[index]) for index in [1, 3, 5]]
                )
    return "".join([stacks[i + 1].pop() for i in range(len(stacks))])
```
