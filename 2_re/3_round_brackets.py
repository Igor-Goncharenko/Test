import re
text = "dog and cat, big dog11 and small cat22"
print(re.findall(r"(dog\w*).+?(cat\w*)", text))
print(re.findall(r"(dog).+?(cat)", text))

text = "Id = 2937198; Name = Cool Hat; Weight = 0.3kg; Price = 299$"
print(re.findall(r"(\w+)\s*=\s*([^;]+)", text))
print(re.findall(r"(Name|Price)\s*=\s*([^;]+)", text))
print(re.findall(r"(?:Name|Price)\s*=\s*([^;]+)", text))
print(re.search(r"(Name)\s*=\s*(?P<name>[^;]+)", text).groupdict())

