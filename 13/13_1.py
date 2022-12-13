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


print(distress_signal(), distress_signal()==6428)