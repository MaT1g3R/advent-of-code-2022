from pathlib import Path
import __main__


def get_input() -> str:
    day = __main__.__file__.replace("py", "txt")
    return (Path("data") / day).read_text()


def lines(s):
    for l in s.splitlines():
        if l:
            yield l


class Solve:
    def __init__(self, example_input, part1, part2):
        self.input = get_input()
        self.example_input = example_input
        self.part1 = part1
        self.part2 = part2

    def solve(self):
        print(
            "part1: ",
            "example input: ",
            self.part1(self.example_input),
            " input: ",
            self.part1(self.input),
        )
        print(
            "part2: ",
            "example input: ",
            self.part2(self.example_input),
            " input: ",
            self.part2(self.input),
        )
