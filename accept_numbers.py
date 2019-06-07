# case 1 accept 10 members and ignore invalid numbers
sum = 0
i = 0
for n in range(0, 10):
    l = input("Enter a number : ")
    try:
        num = int(l)

    except ValueError:
        print(f"{l} is ignored because it is not a integer")
    else :
        i = i + 1
        sum += num
    finally:
        n = n + 1

print(f"Average of the Numbers is : {sum / i}")
