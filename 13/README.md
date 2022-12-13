# Day 13: Distress Signal

[instructions](https://adventofcode.com/2022/day/13)

## Part One

Today's problem was really simple since Python can easily evaluate and transform a string to complex variable definition.
That way, we only need to recursively check every value in both element of the pair:

```python
import ast


def field_compare(a,b):
    if(type(a) == list and type(b) == list):
        for index in range(max(len(a), len(b))):
            if(index >= len(a) or index >= len(b)):
                return (index >= len(a)) - (index >= len(b))
            result = field_compare(a[index], b[index])
            if(result == -1 or result == 1):
                return result
    elif(type(a) == list and type(b) != list ):
        return field_compare(a, [b])
    elif(type(a) != list and type(b) == list ):
        return field_compare([a], b)
    else:
        return (a < b) - (a > b)

def distress_signal():
    with open("./input") as file:
        lines = [line.split() for line in file.read().split("\n\n")]
        valid = 0
        for index,line in enumerate(lines):
            a,b = ast.literal_eval(line[0]),ast.literal_eval(line[1])
            if(field_compare(a,b) >= 0):
                valid += (index+1)
        return valid
```

Note:
- if `b` is greater than `a` `field_compare` returns `1`
- if `a` is greater than `b` `field_compare` returns `-1`
- if `a` is equal to `b` `field_compare` returns `0`

## Part Two

Given the approach I had for part one, the second part was even easier :
```python
import functools
import ast


def field_compare(a,b):
    if(type(a) == list and type(b) == list):
        for index in range(max(len(a), len(b))):
            if(index >= len(a) or index >= len(b)):
                return (index >= len(a)) - (index >= len(b))
            result = field_compare(a[index], b[index])
            if(result == -1 or result == 1):
                return result
    elif(type(a) == list and type(b) != list ):
        return field_compare(a, [b])
    elif(type(a) != list and type(b) == list ):
        return field_compare([a], b)
    else:
        return (a < b) - (a > b)


def distress_signal():
    with open("./input") as file:
        divider_packets = [[[2]],[[6]]]
        lines = [ast.literal_eval(packet) for line in file.read().split("\n\n") for packet in line.split() ]
        lines.extend(divider_packets)
        
        lines = sorted(lines, key=functools.cmp_to_key(field_compare))[::-1]

        position = 1
        for packet in divider_packets:
            position *= (lines.index(packet)+1)
        return position
```

Some details:
- `sorted(lines, key=functools.cmp_to_key(field_compare))[::-1]` allows us to sort the packet using `field_compare` as a custom sorting function
- `[::-1]` reverse the list order. It would have been possible to just change the value returned by `field_compare` but I'm too lazy for that