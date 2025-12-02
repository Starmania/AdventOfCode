import os

os.chdir(os.path.dirname(__file__))

inp = open("input.txt").read().strip("\n ").split(",")


def solve(puzzle_input: list[str]):
    counter = 0
    for part in puzzle_input:
        a, b = part.split("-")
        for i in range(int(a), int(b) + 1):
            s = str(i)
            if len(s) % 2 == 0 and s[: len(s) // 2] == s[len(s) // 2 :]:
                counter += i

    return counter


print(solve(inp))
