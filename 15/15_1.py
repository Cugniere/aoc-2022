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
print(beacon_exclusion_zone())
