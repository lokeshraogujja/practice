# accept a string and count the number of vowels in them
count = 0
s = input("Enter a Sentence of your choice : ")
n = len(s)
print(f"the Number of characters in the given string : {n}")
for i in s:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        count += 1
print(f"The Number of Vowels in the Given Sentence is : {count}")
