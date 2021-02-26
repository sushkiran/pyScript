import re

str = ' Braund, Mr.Owen Harris, 1'
x = re.split('[,.]',str)
o = list(map(lambda z: z.strip(),x))
print(o)