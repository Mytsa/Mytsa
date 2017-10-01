import re
text = raw_input("input you text: ")
find = raw_input("input symbols for search: ")

s1 = l = text.split()

r = re.compile(find)
rs = [w for w in filter(r.match, s1)]
print rs
