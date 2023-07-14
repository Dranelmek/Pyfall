'''
helpful tools to make the code more readable
'''

# preset scryfall api routes
routes = {
    'default': 'https://api.scryfall.com/',
    'cards_generic': 'https://api.scryfall.com/cards',
    'random': 'https://api.scryfall.com/cards/random',
    'cards': 'https://api.scryfall.com/cards/named'
}

# this function will autogenerate an api link
def links(route=routes['cards'], exact=False, set=None, name="fblthp-the-lost"):

    link = f"{route}?{'exact' if exact else 'fuzzy'}={name}"
    return link