# have to get 10 numbers any way
sum = 0
i = 0
while True:
    l = input("Enter a number : ")
    try:
        num = int(l)

    except ValueError:
        print(f"{l} is ignored because it is not a integer")
    else :
        i = i + 1
        sum += num
    finally:
        if i == 10 :
            break

print(f"Average of the Numbers is : {sum / 10}")
