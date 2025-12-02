import os

os.chdir(os.path.dirname(__file__))

inp = open("input.txt").read()


def solve(puzzleInput: str) -> int:
    rotation = 50
    counter = 0
    for line in puzzleInput.split():
        if line[0] == "R":
            rotation += int(line[1:])
        else:
            rotation -= int(line[1:])
        if rotation % 100 == 0:
            counter += 1

    return counter


print(solve(inp))
