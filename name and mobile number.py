# accept names and mobile number from the user and display them in a sorted order

details = {}
while True:
    n = input("Enter the name of the costumer (press end to stop) : ")
    if n == "end":
        break
    m = int(input("Enter the mobile number of the costumer : "))
    details[n] = m
print(f"The Details of the Costumers are : {details}")


