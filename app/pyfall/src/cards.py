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
            try:
                cardtype = data['card']
            except:
                raise ApiError("Error populating card object")
            # generic values
            self.name = data['name']
            self.cost = data['mana_cost']
            self.cmc = data['cmc']
            self.rulesText = data['oracle_text']
            self.cardTypes = data['type_line']
            self.color = data['colors']

            # type/card specific values
            if("creature" in str(self.cardTypes).lower()):
                self.p = data['power']
                self.t = data['toughness']
            
            if("battle" in str(self.cardTypes).lower()):
                self.defense = data['defense']

            if("planeswalker" in str(self.cardTypes).lower()):
                self.loyalty = data['loyalty']
            
            if(data['flavor_text']):
                self.flavorText = data['flavor_text']

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

# TODO: make get_card method that populates the card class and makes an api call

def get_card(name="", option=0):
    # name is the card name and option will be intergers that decide how specific the request is
    return