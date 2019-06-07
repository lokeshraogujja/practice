# from a text containing names and numbers get numbesr and names
f = open("students.txt", "rt")
details = []
directory = {}
for det in f:
    details.append(det.split(","))

for n in range(0, len(details)):
    sum = 0
    for i in range(1, len(details[n])):
        if details[n][0] in directory:
            directory[details[n][0]].add(details[n][i].strip("\n"))
        else:
            directory[details[n][0]] = {details[n][i].strip("\n")}
for k, v in sorted(directory.items()):
    print(f"{k:10s}  {v}")
