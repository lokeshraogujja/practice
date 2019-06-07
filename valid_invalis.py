# accept entries from user and separate them by valid and invalid
v = open("vald.txt", "wt")
i = open("invalid.txt", "wt")
entries =[]
while True:
    l = input("Enter a Entry (enter stop to stop) : ")
    if l == "stop":
        break
    else:
        entries.append(l)
for f in entries:
    if f.isdigit():
        v.write(f + "\n")
    else:
        i.write(f + "\n")
v.close()
i.close()