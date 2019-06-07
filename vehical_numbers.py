# accept vehicle numbers from user and display valid numbers
import re
vnum = []
while True:
    i = input("Enter a vehicle Number (press stop to stop) : ")
    if i == "stop":
        break
    else:
        try:
            m = re.findall("[A-Z]{2}[ ]+\d{2}[ ]+[A-Z]{2}[ ]+\d{4}",i)
            vnum.extend(m)
        except:
            pass
for l in vnum:
    print(f"The valid vehicle Numbers are : {l}")
