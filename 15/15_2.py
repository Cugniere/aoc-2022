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
print(beacon_exclusion_zone())
