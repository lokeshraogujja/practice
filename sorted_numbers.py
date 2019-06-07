# have to get 10 numbers any way in sorted way
i = 0
last_num = 0
no = []
while True:
    l = input("Enter a number : ")
    try:
        num = int(l)

    except ValueError:
        print(f"{l} is ignored because it is not a integer")
    else :
        i = i + 1
        if num > last_num:
            no.append(num)
    finally:
        last_num = num
        if num == 0 :
            break


print(f"the numbers are : {no}")
