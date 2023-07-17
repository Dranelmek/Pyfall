# TODO: create card class that acts as a template for card information the user will see

# TODO: make card class able to populate itsself and abstract api calls
from errors import *

class Card:
    '''
    The card class is for generating lightweight card
    objects with the necesary data on magic cards. This
    is a superclass for generic cards, each card type will
    be its own class.
    '''
    def __init__(self, data:dict):
        try:
            self.name
            self.cost
            self.cmc
            self.rulesText
        except ApiError as a:
            print(a)
        except:
            print("something went wrong")


class RawCardData:
    '''
    This class can be used to simply generate an object
    with pure scryfall request data.
    '''
    def __init__(self, data:dict):
        try:
            self.data = data
        except ApiError as a:
            print(a)
        except:
            print("something went wrong")
