import requests
from handlers import *

# template code for apicall
# respons = requests.get('https://randomuser.me/api')
# print(respons.status_code)

# result = respons.json()['results'][0]
# name = f"{result['name']['first']} {result['name']['last']}"

# print(name)
# print(links())

# will return the 
def generic_request():
    url = links(route=routes["random"])
    response = requests.get(url)
    result = response.json()
    return result

def specific_request(url):
    response = requests.get(url)
    result = response.json()
    return result

print(generic_request())