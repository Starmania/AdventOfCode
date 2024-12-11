import os

os.chdir(os.path.dirname(__file__))

is_safe = 0


def checkSafe_(numbers: list[int], a, b, joker=True):
    for i in range(len(numbers)-1): 
        if not a < numbers[i] - numbers[i+1] < b:
            if joker:
                for i in range(len(numbers)):
                    if checkSafe(numbers[:i] + numbers[i+1:], joker=False):
                        return 1
            return 0
    print("this is ok:", numbers)
    return 1


def checkSafe(numbers: list[int], joker=True):
    if numbers[0] > numbers[1]:
        return checkSafe_(numbers, 0, 4, joker)
    return checkSafe_(numbers, -4, 0, joker)


with open('input', 'r', encoding="utf8") as f:
    for line in f.readlines():
        nums = list(map(int, line.split()))
        is_safe += checkSafe(nums)

print(is_safe)
