# Advent of Code - 2022

## Day 1 : Calorie counting

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
Since the file is being read line by line memory consumption is minimal and we only need 2 variables to store value between loop:
- `buffer` to store the total amount of calories held by a single Elf
- `max_calorie` to store the maximum amount held by one of the Elf
