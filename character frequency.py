# to conut how many number of time  a character is repeating

freq = {}
s = input("Enter the string to be checked : ")
for c in s:
     if c not in freq :
         cnt = s.count(c)
         freq[c] = cnt
for c,cnt in freq.items():
    print(c,cnt)

