import os
import pprint

os.chdir(os.path.dirname(__file__))


def parseRules(rules: str):
    dic_rules: dict[int, set[int]] = {}
    for rule in rules.split("\n"):
        a_is_before, b = map(int, rule.strip().split("|"))
        if not a_is_before in dic_rules:
            dic_rules[a_is_before] = set()
        dic_rules[a_is_before].add(b)
        # dic_rules[a_is_before].sort()

    return dic_rules


with open("input", encoding="utf8") as file:
    content = file.read().split("\n\n")

rules, orders = content[0], content[1]

RULES = parseRules(rules)
ORDERS = tuple(tuple(map(int, order.split(","))) for order in orders.split())

good = []
for order in ORDERS:
    seen = set()
    for num in order:
        if num in RULES and RULES[num] & seen:
            break
        seen.add(num)
    else:
        good.append(order)

somme = 0
for order in good:
    somme += order[(len(order)//2)]

print(somme)
