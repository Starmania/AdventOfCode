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

bad = []
for order in ORDERS:
    seen: set[int] = set()
    for num in order:
        if num in RULES and RULES[num] & seen:
            bad.append(order)
            break
        seen.add(num)


somme = 0
for order in bad:
    _ = """
    Some hacky tech because if you filter the rules to the important numbers
    you could see that the number of rules is the order of the numbers...
    {13: set(),
    29: {13},
    47: {13, 29},
    75: {29, 13, 47},
    97: {29, 75, 13, 47}}
    """
    numbers = set(order)
    order_ = list(order)
    order_.sort(
        key=lambda num: len(RULES[num] & numbers) if num in RULES else 0,
        reverse=True
    )
    subset_rules = {num: RULES[num] & numbers
                    if num in RULES else set() for num in numbers}
    pprint.pprint(subset_rules, width=30)
    pprint.pprint(order_)
    somme += order[(len(order)//2)]

print(somme)
