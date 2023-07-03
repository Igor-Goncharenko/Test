import re
text = "map fsdjo bitmap"
print(re.findall(r"map", text))
print(re.findall(r"\bmap\b", text))

text = "(food), fastfood, junkfood"
print(re.findall(r"food", text))
print(re.findall(r"\(food\)", text))

text = "Food, fastfood, junkfood"
print(re.findall(r"[fF]oo[d]", text))
print(re.findall(r"\b[fF]ood\b", text))

text = "Example: 8 plus 7 equals 15; -1"
print(re.findall(r"[0-9]", text))
print(re.findall(r"[0-9][0-9]", text))
print(re.findall(r"[-0-9]", text))
print(re.findall(r"-[0-9]", text))
print(re.findall(r"[0-9a-z]", text))

print(re.findall(r"[\d]", text))
print(re.findall(r"[\w]", text))

print(re.findall(r"[^0-9]", text))  # ^0-9  <=>  \D
print(re.findall(r"[^\w]", text))  # ^\w  <=>  \W


