from errors import *
from handlers import *
from api import *

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
                dataType = data['object']
            except:
                raise ApiError("Error populating card object")
            # generic values
            self.name = data.get('name', None)
            self.cost = data.get('mana_cost', None)
            self.cmc = data.get('cmc', None)
            self.rulesText = data.get('oracle_text', None)
            self.cardTypes = data.get('type_line', None)
            self.color = data.get('colors', None)
            self.flavorText = data.get('flavor_text', None)
            self.setName = data.get('set_name', None)
            self.set = data.get('set', None)
            self.p = data.get('power', None)
            self.t = data.get('toughness', None)
            self.defense = data.get('defense', None)
            self.loyalty = data.get('loyalty', None)

            
        except ApiError as a:
            print(a)
        
    
    def __call__(self, *args, **kwds):
        pass

    def __str__(self):
        newLine = "\n"
        pt = None
        if (self.p and self.t):
            pt = f'{self.p}/{self.t}'
        return (
            f'{self.name}\t{self.cost if self.cost else ""}\n'
            f'\n'
            f'{self.cardTypes}\t{self.set}\n'
            f'\n'
            f'{self.rulesText}\n'
            f'\n'
            f'{(self.flavorText + newLine) if self.flavorText else ""}'
            f'\t{(self.defense + newLine) if self.defense else ""}'
            f'\t{(self.loyalty + newLine) if self.loyalty else ""}'
            f'\t{(pt + newLine) if pt else ""}'
        )


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

def get_card(name="", setName="", option=0):
    
    out = None

    # name is the card name and option will be intergers that decide how specific the request is
    match option:
        case 0:
            out = Card(random_request())
        case 1:
            out = Card(generic_request(name))
        case 2:
            out = Card(set_specific_request(name, setName))
    return out

print(get_card(name="fiery impulse", option=1))