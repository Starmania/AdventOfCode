import os

os.chdir(os.path.dirname(__file__))

inp = open("input.txt").read().strip("\n ").split(",")


def solve(puzzle_input: list[str]):
    counter = 0
    for part in puzzle_input:
        a, b = part.split("-")
        for i in range(int(a), int(b) + 1):
            s = str(i)

            for n in range(1, len(s)):
                dup = s[:n] * (len(s) // n)
                if s == dup:
                    print(f"Matched {s} with {s[:n]} repeated {len(s) // n} times")
                    counter += i
                    break

    return counter


print(solve(inp))
