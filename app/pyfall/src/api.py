import requests
import handlers

# template code for apicall
# respons = requests.get('https://randomuser.me/api')
# print(respons.status_code)

# result = respons.json()['results'][0]
# name = f"{result['name']['first']} {result['name']['last']}"

# print(name)
# print(links())

# scryfall api requests
def generic_request(cardName):
    url = handlers.links(name=cardName)
    response = requests.get(url)
    result = response.json()
    handlers.api_error(result)
    return result

def set_specific_request(cardName, setName):
    url = handlers.links(name=cardName, set=setName)
    response = requests.get(url)
    result = response.json()
    handlers.api_error(result)
    return result

def full_specific_request(url):
    response = requests.get(url)
    result = response.json()
    handlers.api_error(result)
    return result

def random_request():
    url = handlers.links(route=handlers.routes["random"])
    response = requests.get(url)
    result = response.json()
    handlers.api_error(result)
    return result


# print(generic_request("teferi, time raveler")['oracle_text'])
# print(generic_request("hullbreacher")['set_name'])