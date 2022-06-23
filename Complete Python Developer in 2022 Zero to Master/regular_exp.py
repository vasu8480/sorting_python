import re

pattern =re.compile('[a-zA-Z]')
str='hi vasu how do you?'

a=pattern.findall(str)
b=pattern.search(str)
c=pattern.fullmatch(str)
b=pattern.search(str)
print(b.group())



