import re 
x = re.findall("[-+]?\d+.\d+|[-+]?\d+", "Current Level: -13.1 db or 14.2 or -3 or +12")
print(x)
y = list(map(float,x))
print(y)
