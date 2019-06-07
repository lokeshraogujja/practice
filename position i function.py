# accept two list an tell the position of each term
def position(l1, l2):
    n = input("Enter the number of l2 to be checked :")
    if n in l1:
        print(f"The position of the number is : {l1.index(n)}")


list1 = []
list2 = []

while True:
    m = int(input("Eneter the numbers of list 1 (press 0 to stop) : "))
    if m == 0 :
        break
    list1.append(m)

while True:
    l = int(input("Eneter the numbers of list 2 (press 0 to stop) : "))
    if l == 0 :
        break
    list1.append(l)
position(list1,list2)
