# accept names and mobile numbers also names should support multiple numbers

details = {}
i = 0
while True:
    n = input("Enter the name of the costumer (press end to stop) : ")
    if n == "end":
        break
    m = input("Enter the mobile number of the costumer : ")
    if n in details:
        details[n].add(m)
    else:
        details[n] = {m}
for n,m in details.items():
    print(f"{n:10s} - {' - '.join(m)}")



