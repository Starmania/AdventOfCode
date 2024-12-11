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
setA = set(listA)

scoresB = {a: listB.count(a)*a for a in setA}
for a in listA:
    sum_diff += scoresB[a]

print(sum_diff)
