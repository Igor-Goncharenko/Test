"""
{m,n}
m - minimum number of matches
n - maximum number of matches

{m,n}? - minor quantifier (takes minimum number of matches)

{m} - exactly 'm' times
{m,} - 'm' and more time
{,n} - no more than 'n' time

? - from 0 to 1 ({0,1})
* - from 0 and more ({0,})
+ - from 1 and more ({1,})
?? *? +? - minor mode
"""
import re
text = "Gogle, Google, Goooogle, Gooooooogle"
print(re.findall(r"o{2,}", text))
print(re.findall(r"o{2,}?", text))
print(re.findall(r"Go{2,}gle", text))
text = "Goooogleooogle"
print(re.findall(r"G[a-z]{0,}gle", text))
print(re.findall(r"G[a-z]{0,}?gle", text))
print(re.findall(r"G[a-z]*gle", text))
print(re.findall(r"G[a-z]*?gle", text))


text = "Id = 2937198; Name = Cool Hat; Weight = 0.3kg; Price = 299$"
print(re.findall(r"\w+\s*=\s*[^;]+", text))
print(text.split(";"))

text = "<p> Interesting image <img src= 'img.png'> Wow!</p> <img>"
print(re.findall(r"<img.+src\s*=\s*[^>]+>", text))


