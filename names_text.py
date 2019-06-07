# accept a list of number and print them in names.txt in sorted order
n = open("names.txt", "wt")
names = []
while True:
    m = input("Enter a Name (Press ENd to stop) :")
    if m == "end":
        break
    else:
        names.append(m)
for l in sorted(names):
    n.write(l + "\n")
n.close()
