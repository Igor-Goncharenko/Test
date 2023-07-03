import re
# match
text = "+7(951)456-43-95"
m = re.match(r"\+7\(\d{3}\)\d{3}-\d{2}-\d{2}", text)
print(m)

# split
text = "word1; word2, word3: word4"
m = re.split(r"\s*[:;,]+\s*", text)
print(m)

# sub
text = "Moscow Saint-Petersburg Kazan Vladivostok Chelyabinsk"
m = re.sub(r"\s*([-\w]+)\s*", r"<city>\1</city>", text)
print(m)

count = 0
def repl_find(m):
    global count
    count += 1
    return f"<city number='{count}'>{m.group(1)}</city>"
m = re.sub(r"\s*([-\w]+)\s*", repl_find, text)
print(m)

m, c = re.subn(r"\s*([-\w]+)\s*", r"<city>\1</city>", text)
print(m, c)

rx = re.compile(r"\s*([-\w]+)\s*")
m = rx.sub(r"<city>\1</city>", text)
print(m)
