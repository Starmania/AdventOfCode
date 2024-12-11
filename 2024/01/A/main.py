import os

os.chdir(os.path.dirname(__file__))

sum_diff = 0
listA = []
listB = []

with open('input', 'r', encoding="utf8") as f:
    for line in f.readlines():
        a, b = map(int, line.split())
        listA.append(a)
        listB.append(b)

listA.sort()
listB.sort()

for i in range(len(listA)):
    a, b = listA[i], listB[i]
    if a > b:
        sum_diff += a-b
    else:
        sum_diff += b-a

print(sum_diff)
