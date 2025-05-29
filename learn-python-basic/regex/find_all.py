import re

txt = "The rain in Spain aing"
x = re.findall("ai", txt)
print(x)

x = re.findall("Portugal", txt)
print(x)