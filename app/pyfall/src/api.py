import requests
from handlers import *

# template code for apicall
respons = requests.get('https://randomuser.me/api')
print(respons.status_code)

result = respons.json()['results'][0]
name = f"{result['name']['first']} {result['name']['last']}"

print(name)
print(links())
