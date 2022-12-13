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


print(distress_signal(), distress_signal()==22464)