import os

os.chdir(os.path.dirname(__file__))


def check_pattern(last_position: tuple[int, int], i, j):
    if not 0 <= last_position[0] + i < CONTENT_LENGHT:
        return False
    if not 0 <= last_position[1] + j < LINE_LENGTH:
        return False
    return True


# PATTERNS ([i][j] == "X"):
PATTERNS = [
    # Horizontal
    ((0, 1), (0, 2), (0, 3)),
    ((0, -1), (0, -2), (0, -3)),

    # Vertical
    ((1, 0), (2, 0), (3, 0)),
    ((-1, 0), (-2, 0), (-3, 0)),

    # Diagonales (4)
    ((1, 1), (2, 2), (3, 3)),  # Bas droite
    ((1, -1), (2, -2), (3, -3)),  # Bas gauche
    ((-1, 1), (-2, 2), (-3, 3)),  # Haut droite
    ((-1, -1), (-2, -2), (-3, -3))  # Haut gauche
]

with open("input", encoding="utf8") as file:
    content = file.readlines()

content = [line.strip() for line in content]

CONTENT_LENGHT = len(content)
LINE_LENGTH = len(content[0])

counter = 0

for i in range((CONTENT_LENGHT)):
    for j in range((LINE_LENGTH)):
        if content[i][j] != "X":
            continue

        for pattern in PATTERNS:
            if check_pattern(pattern[-1], i, j):
                if content[pattern[0][0] + i][pattern[0][1] + j] != "M":
                    continue
                if content[pattern[1][0] + i][pattern[1][1] + j] != "A":
                    continue
                if content[pattern[2][0] + i][pattern[2][1] + j] != "S":
                    continue
                counter += 1

print(counter)
