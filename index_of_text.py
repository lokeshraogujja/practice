f = open("index.txt", "rt")
names = []
for l in f:
    names.append(l.strip("\n"))

for n in range(0, len(names)):
    names[n].split(" ")
