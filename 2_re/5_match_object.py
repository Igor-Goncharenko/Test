import re
with open("text.html", encoding="utf-8") as file:
    text = file.read()
match = re.search(r"<link[ \t]+(.+)(?<=>)", text)
print(match)
print(match.group())
print(match.lastindex)
print(match.group(0), match.group(1))
print(match.group(0, 1))
print(match.start(0), match.end(0), match.span(0))
print(match.regs)
print(match.pos, match.endpos)
# print(match.string)
print(match.re)
print(match.lastgroup)

match = re.search(r"(?P<key>\w+)[ \t]*=[ \t]*[\"'](?P<value>[^\"']+)(?<![ \t])", text)
print(match.groupdict())
matches = [match for match in re.finditer(r"(?P<key>\w+)[ \t]*=[ \t]*[\"'](?P<value>[^\"']+)(?<![ \t])", text)]
print(matches[3].groupdict())

