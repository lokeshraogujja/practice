# accept names and show them in a list in asorted way
names = []
while True:
    m = input("Enter a Name : ")
    if m == 'end' or m == 'END' or m == 'End':
        break
    else:
        names.append(m)
names.sort()
print(names)
