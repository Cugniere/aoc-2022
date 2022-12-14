# Day 1: Calorie counting

[instructions](https://adventofcode.com/2022/day/1)

## Part One

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
                buffer += int(line.rstrip())
    return buffer if buffer > max_calorie else max_calorie
``` 
Since the file is being read line by line memory consumption is minimal and we only need 2 variables to store values between loop:
- `buffer` to store the total amount of calories held by a single Elf
- `max_calorie` to store the maximum amount held by one of the Elf

## Part Two

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
                buffer += int(line.rstrip())
    return sum(stack_insert(buffer))
``` 
