import re

txt = "The rain in Spain"
x = re.split("\\s", txt)
print(x)


x = re.split("\\s", txt, 1)
print(x)