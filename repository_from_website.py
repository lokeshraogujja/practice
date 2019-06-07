import requests
import sys

id = input("Enter  id : ")
resp = requests.get(f"https://api.github.com/users/{id}/repos")
if resp.status_code != 200:
    print("sorry A Error as Occurred")
    sys.exit(1)
else:
    repos = resp.json()
    for r in repos:
       print(f"{r['name']:50}")