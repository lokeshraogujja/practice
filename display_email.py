# from persons.txt display details if both are present
import re

f = open("persons.txt", "rt")
details = {}
for nam in f.readlines():

    m = re.search("(\w+\W\w+\W\w+)\W+(\d+)", nam)
    for i in range(0, len(m)):
        details[m[i][0]] = m[i][1]

f.close()

for k, v in sorted(details.items()):
    print(f"{k:25s}{v}")
