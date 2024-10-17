import re
files = ["a.txt", "b.txt", "c.txt"]

for filename in files:
    file = open(filename, 'r')
    content = file.read()
    print(content)