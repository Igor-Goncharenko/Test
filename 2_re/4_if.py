import re
# text = "football, basketball, foot, ball"
# print(re.findall(r"(foot|ball)", text))
# print(re.findall(r"\b(foot|ball)\b", text))

with open("text.html", encoding="utf-8") as file:
    text = file.read()
print(re.findall(r"<script.*?>[\w\W]*?(?=</script>)", text, re.MULTILINE))
print(re.findall(r"<script.*?>[\w\W]*?(?<=</script>)", text, re.MULTILINE))
match = re.findall(r"([-\w]+)\s*=\s*[\"']([^\"']+)(?<![ \t])", text)
print(len(match), match)
# ?(id|name)yes_pattern|no_pattern
match = re.findall(r"([-\w]+)\s*=\s*(?P<q>[\"'])?(?(q)([^\"']+(?<![ \t>]))|([^ \t>]+))", text)
print(len(match), match)

