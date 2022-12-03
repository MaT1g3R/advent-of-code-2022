from pathlib import Path
from string import ascii_letters
from collections import Counter

input_ = Path("data/day3.txt").read_text()
example_input = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


priorities = {c: i + 1 for i, c in enumerate(ascii_letters)}


def lines(i):
    for line in i.splitlines():
        line = line.strip()
        if line:
            yield line


def parse_input(i):
    for line in lines(i):
        l = len(line)
        yield line[: l // 2], line[l // 2 :]


class Input2:
    def __init__(self, i):
        self.i = lines(i)

    def __next__(self):
        return next(self.i), next(self.i), next(self.i)

    def __iter__(self):
        return self


def part1(i):
    s = 0

    for a, b in parse_input(i):
        a, b = set(a), set(b)
        for item in a:
            if item in b:
                s += priorities[item]

    return s


def part2(i):
    s = 0
    for a, b, c in Input2(i):
        a, b, c = set(a), set(b), set(c)
        d = a.intersection(b).intersection(c)
        s += priorities[d.pop()]
    return s


if __name__ == "__main__":
    i = input_
    print("a", part1(i))
    print("b", part2(i))
