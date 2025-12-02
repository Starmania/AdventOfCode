import os

os.chdir(os.path.dirname(__file__))

inp = open("input.txt").read()


def solve(puzzleInput: str) -> int:
    rotation = 50
    counter = 0

    for line in puzzleInput.split():
        l = 1

        if line[0] == "L":
            l = -1

        for _ in range(int(line[1:])):
            rotation += l
            if not rotation % 100:
                counter += 1

    return counter


print(solve(inp))
