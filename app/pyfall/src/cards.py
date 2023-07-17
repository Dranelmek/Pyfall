from errors import *

class Card:
    '''
    The card class is for generating lightweight card
    objects with the necesary data on magic cards. 
    depending on the card type certain values will be set to none
    '''
    # TODO: finish init function and make it set the object properties

    def __init__(self, data:dict):
        try:
            # generic values
            self.name
            self.cost
            self.cmc
            self.rulesText
            self.cardTypes
            self.flavorText
            self.color

            # type specific values
            self.p
            self.t
            self.loyalty
            self.defense


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
