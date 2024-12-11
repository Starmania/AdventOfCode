import re
import os


os.chdir(os.path.dirname(__file__))

regex = r"mul\((\d+),(\d+)\)"
with open("input", "r", encoding="utf8") as file:
    matches = re.finditer(regex, file.read())

somme = 0

for match in matches:
    somme += int(match.group(1))*int(match.group(2))

print(somme)
