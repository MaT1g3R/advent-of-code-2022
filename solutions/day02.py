from pathlib import Path

input_ = Path("data/day2.txt").read_text()


rock = "A"
paper = "B"
sissors = "C"


draw = 3
win = 6

scores = {
    rock: 1,
    paper: 2,
    sissors: 3,
}


plays = [s.strip() for s in input_.splitlines() if s]


def part1():
    m = {
        "X": "A",
        "Y": "B",
        "Z": "C",
    }
    total = 0
    for line in plays:
        oppo, _, us = line.partition(" ")
        us = m[us]
        total += scores[us]

        match [oppo, us]:
            case "A", "B":
                total += win
            case "B", "C":
                total += win
            case "C", "A":
                total += win
            case _ if oppo == us:
                total += draw
    return total


def part2():
    total = 0
    for line in plays:
        oppo, _, us = line.partition(" ")

        match oppo, us:
            case ["A", "X"]:
                total += scores[sissors]
            case ["B", "X"]:
                total += scores[rock]
            case ["C", "X"]:
                total += scores[paper]
            case ["A", "Z"]:
                total += win
                total += scores[paper]
            case ["B", "Z"]:
                total += win
                total += scores[sissors]
            case ["C", "Z"]:
                total += win
                total += scores[rock]
            case [oppo, "Y"]:
                total += draw
                total += scores[oppo]

    return total


if __name__ == "__main__":
    print("a", part1())
    print("b", part2())
