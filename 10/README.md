# Day 10: Cathode-Ray Tube

[instructions](https://adventofcode.com/2022/day/10)

## Part One

The hardest part of the problem is understand the instructions correctly.

Not much to say about the code, it is only a baisc loop with some conditions:
```python
def cpu_instructions():
    with open("./input") as file:
        signal_strengths = []
        value = 1
        cycle = 0
        for line in file:
            cycle += 1
            if (cycle - 20) % 40 == 0 and cycle <= 220:
                signal_strengths.append(cycle * value)
            if line.rstrip() != "noop":
                cycle += 1
                if (cycle - 20) % 40 == 0 and cycle <= 220:
                    signal_strengths.append(cycle * value)
                value += int(line.rstrip().split(" ")[1])
        return sum(signal_strengths)
```

## Part Two

Not much to say about part two either, I find today problems way easier than the previous day.
```python
def cpu_instructions(width=40, height=6):
    def draw_pixel(value, cycle, screen):
        position = (cycle - 1) % width
        if position in {value - 1, value, value + 1}:
            screen[cycle - 1] = "#"

    with open("./input") as file:
        screen = ["."] * (width * height)

        value = 1
        cycle = 0
        for line in file:
            cycle += 1
            draw_pixel(value, cycle, screen)
            if line.rstrip() != "noop":
                cycle += 1
                draw_pixel(value, cycle, screen)
                value += int(line.rstrip().split(" ")[1])

        for line in [
            screen[index : index + width] for index in range(0, len(screen), width)
        ]:
            print("".join(line))
```
The solution may be hard to read for someone with a visual impairement:
```text
###..#....####.####.#..#.#....###..###..
#..#.#....#....#....#..#.#....#..#.#..#.
#..#.#....###..###..#..#.#....#..#.###..
###..#....#....#....#..#.#....###..#..#.
#....#....#....#....#..#.#....#....#..#.
#....####.####.#.....##..####.#....###..
```
