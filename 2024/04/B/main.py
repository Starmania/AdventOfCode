import os

os.chdir(os.path.dirname(__file__))

# PATTERNS ([i][j] == "A"):


with open("input", encoding="utf8") as file:
    content = file.readlines()

content = [line.strip() for line in content]

CONTENT_LENGHT = len(content)
LINE_LENGTH = len(content[0])

counter = 0

PAS_BRANCHE = ("X", "A")

for i in range(1, CONTENT_LENGHT-1):
    for j in range(1, LINE_LENGTH-1):
        if content[i][j] != "A":
            continue

        if content[i-1][j-1] in PAS_BRANCHE:
            continue
        if content[i+1][j+1] in PAS_BRANCHE:
            continue

        if content[i-1][j-1] == content[i+1][j+1]:
            continue

        if content[i-1][j-1] == content[i-1][j+1]:
            if content[i+1][j-1] == content[i+1][j+1]:
                # M.M
                # .A.
                # S.S
                counter += 1
        elif content[i-1][j-1] == content[i+1][j-1]:
            if content[i-1][j+1] == content[i+1][j+1]:
                # M.S
                # .A.
                # M.S
                counter += 1

print(counter)
