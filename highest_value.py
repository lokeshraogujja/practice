# to set both the number to the highest of them

a = int(input("Enter the First Number : "))
b = int(input("Enter The Second Number : "))
print(f"The Input Numbers are : {a} {b}")

if a > b:
    b = a
else:
    a=b
print(f"The Required Numbers : {a} {b}")

