from collections import deque
from aoc import aoc

example_input = """
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""


def parse_input(i):
    stacks, moves = [], []
    for line in i.splitlines():
        if not line:
            continue
        if line.startswith("move"):
            cur_move = []
            move = line.split()
            for s in move:
                try:
                    cur_move.append(int(s))
                except ValueError:
                    pass
            moves.append(cur_move)
        else:
            stacks.append(line)
    return parse_stack(stacks), moves


def parse_stack(s):
    def parse_line(l, num_stacks):
        row = [None] * num_stacks
        for i in range(num_stacks):
            if not l:
                break
            obj = l[1]
            if obj != " ":
                row[i] = obj
            l = l[3:]
            if not l:
                break
            else:
                l = l[1:]

        return row

    num_stacks = int(s[-1].split()[-1])
    stacks = [deque() for _ in range(num_stacks)]
    for line in s[:-1]:
        row = parse_line(line, num_stacks)
        for i, r in enumerate(row):
            if r:
                stacks[i].append(r)
    return stacks


def part1(i):
    stacks, moves = parse_input(i)
    for amount, from_, to in moves:
        for _ in range(amount):
            o = stacks[from_ - 1].popleft()
            stacks[to - 1].appendleft(o)
    return "".join(s[0] for s in stacks)


def part2(i):
    stacks, moves = parse_input(i)
    for amount, from_, to in moves:
        to_move = []
        for _ in range(amount):
            to_move.append(stacks[from_ - 1].popleft())
        for o in reversed(to_move):
            stacks[to - 1].appendleft(o)
    return "".join(s[0] for s in stacks)


if __name__ == "__main__":
    aoc.Solve(example_input, part1, part2).solve()
