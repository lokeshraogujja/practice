import requests as rs
import sys

pop = []


def Nmaxelements(list1, N):
    final_list = []

    for i in range(0, N):
        max1 = 0

        for j in range(len(list1)):
            if list1[j] > max1:
                max1 = list1[j]
        list1.remove(list1[j])
        final_list.append(max1)
        for u in final_list:
            print(u)


resp = rs.get("https://restcountries.eu/rest/v2/all")
high = []
if resp.status_code != 200:
    print("Sorry Error as occured")
    sys.exit(1)
else:
    countries = resp.json()
    for c in countries:
        pop.append(c['population'])
        Nmaxelements(pop, 10)
