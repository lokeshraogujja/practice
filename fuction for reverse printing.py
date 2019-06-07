# create a function to accept a string and print it in reverse order

def reverse_strng(name, case='n'):
    if case == 'n':
        for c in name[::-1]:
            print(c)
    if case == 'u':
        for c in name[::-1].upper():
            print(c)
    if case == 'l':
        for c in name[::-1].lower():
            print(c)


n = input("Enter the string to be reversed : ")
c = input("Enter a character (u for upper case and l for lower case) : ")
reverse_strng(n,c)