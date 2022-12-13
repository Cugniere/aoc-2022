# Day 6: Tuning Trouble

[instructions](https://adventofcode.com/2022/day/6)

## Part One

Today's problem is really basic, we only need to be sure that all characters in a subarray are different:
```python
def tuning_trouble(signal_length):
    with open("./input") as file:
        line = file.read()
        for index in range(len(line) - signal_length):
            if len(set(line[index : index + signal_length])) == signal_length:
                return index + signal_length
```

It could technically be possible to optimize the search by skipping some index if we know that they are going to contains the same char (for example if we have `abcc` at index `0` we know that we could skip to index `3`) but I'm way too lazy to implement that functionnality.

## Part Two

Same as previous part except we need to call the function with `signal_length = 14`.
