from pathlib import Path

input_ = Path("data/day1.txt").read_text()


def elf(s):
    return [int(line.strip()) for line in s.splitlines() if line.strip()]


elves = [elf(s) for s in input_.split("\n\n") if s.strip()]


def part2():
    sums = [sum(e) for e in elves]
    third, second, first = sorted(sums[:3])

    for e in sums[3:]:
        if e > first:
            first, second, third = e, first, second
        elif e > second:
            first, second, third = first, e, second
        elif e > third:
            first, second, third = first, second, e

    return first, second, third


if __name__ == "__main__":
    print("a:", max(map(sum, elves)))
    print("b:", sum(part2()))
