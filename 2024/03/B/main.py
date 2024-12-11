import re
import os


os.chdir(os.path.dirname(__file__))

with open("input", "r", encoding="utf8") as file:
    content = file.read()

regex = r"don't\(\)(.|\n)*?do\(\)"
content = re.sub(regex, "", content, 0, re.MULTILINE)

regex = r"mul\((\d+),(\d+)\)"
matches = re.finditer(regex, content)

somme = 0

for match in matches:
    somme += int(match.group(1))*int(match.group(2))

print(somme)
