from aoc import aoc

example_input = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


def get_range(s):
    a, b = s.split("-")
    return int(a), int(b)


def contains(a, b):
    a1, a2 = a
    b1, b2 = b

    return a1 <= b1 and a2 >= b2


def overlaps(a, b):
    a1, a2 = a
    b1, b2 = b

    if b1 <= a1 <= b2:
        return True
    if b1 <= a2 <= b2:
        return True


def part1(i):
    total = 0
    for l in aoc.lines(i):
        a, b = l.split(",")
        a, b = get_range(a), get_range(b)

        if contains(a, b) or contains(b, a):
            total += 1
    return total


def part2(i):
    total = 0
    for l in aoc.lines(i):
        a, b = l.split(",")
        a, b = get_range(a), get_range(b)

        if overlaps(a, b) or overlaps(b, a):
            total += 1
    return total


if __name__ == "__main__":
    aoc.Solve(
        example_input,
        part1,
        part2,
    ).solve()
