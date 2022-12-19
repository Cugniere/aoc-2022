# Day 15: Beacon Exclusion Zone

[instructions](https://adventofcode.com/2022/day/15)

## Part One

In my opinion today's problem was the most challenging since the beginning of advent of code 2022. The first part goal was to compute where the beacon could not be on a specific line; my solution could be way faster if I only computed exclusion ranges using the location of each beacon but I ended computing the whole line out of simplicity:

```python
import re


def beacon_exclusion_zone():
  with open("./input") as file:
    grid_min = 0
    grid_max = 0
    lines = file.read().split("\n")[:-2]
    sensors = []
    signals = []
    target = 2000000

    for line in lines:
      sx,sy,bx,by = [int(value) for value in re.findall("-?\d+", line)]
      beacon_range = abs(bx-sx)+abs(by-sy)
      grid_min = min(grid_min,sx,bx-beacon_range)
      grid_max = max(grid_max,sx,bx+beacon_range)
      signals.append((bx,by))
      sensors.append((sx,sy,beacon_range))
    occupied_tiles = 0
    for x in range(grid_min, grid_max):
      if(
        any([abs(sensor[0]-x)+abs(sensor[1]-target) <= sensor[2] for sensor in sensors])
        and (x,target) not in signals
      ):
        occupied_tiles += 1
    return occupied_tiles
```

It takes a few seconds for the script to complete, which is way to high considering the mindset of advent of code.

## Part Two

I took me some time to figure out the solution for part two. I tried to reuse the code from part one as is, computing each cell on the grid but I gave up after 5 minutes of running the script. 

In the end I only check every cell in each sensor range radius plus one, since we know that the only possible cell will be outside any sensor range:

```python
import re


def beacon_exclusion_zone():
  with open("./input") as file:
    lines = file.read().split("\n")[:-2]
    sensors = []
    signals = []
    target_max = 4000000
    for line in lines:
      sx,sy,bx,by = [int(value) for value in re.findall("-?\d+", line)]
      beacon_range = abs(bx-sx)+abs(by-sy)
      signals.append((bx,by))
      sensors.append((sx,sy,beacon_range))
    for sensor in sensors:
      x,y,r = sensor
      for i in range(-r-1, r+2):
        br_x = x + i
        if(br_x < 0 or br_x > target_max):
          continue
        for alt in [-1,1]:
          br_y = y+(alt*(r - abs(i) +1))

          if(
            br_y >= 0
            and br_y <= target_max
            and not any([abs(sensor[0]-br_x)+abs(sensor[1]-br_y) <= sensor[2] for sensor in sensors])
            and (br_x, br_y) not in signals
           ):
            return (br_x,br_y, (br_x*target_max)+br_y)
```


