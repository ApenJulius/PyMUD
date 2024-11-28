import uuid
#import skills
import random
import copy
from config import ItemType, EquipmentSlotType, StatType


# load an item either from 
def load_item(item):
    item = copy.deepcopy(item)
    item_type = item['item_type']
    #print(item_type)

    if item_type == ItemType.EQUIPMENT:
        new_item = Equipment()
        #template = Equipment()

        #new_item.item_type = item['item_type']
        new_item.name = item['name']
        new_item.description = item['description']

        new_item.stats = item['stats']
        new_item.requirements = item['requirements']

        new_item.slot = item['slot']
        new_item.equiped = item['equiped']
        new_item.tags = item['tags']
        new_item.history = item['history']


    if item_type == ItemType.MISC:
        new_item = Item()

        #new_item.item_type = item['item_type']
        new_item.name = item['name']
        new_item.description = item['description']
        new_item.tags = item['tags']
        new_item.history = item['history']

    if item_type == ItemType.CONSUMABLE:
        new_item = Consumable()

        #new_item.item_type = item['item_type']
        new_item.name = item['name']
        new_item.description = item['description']
        new_item.tags = item['tags']
        new_item.history = item['history']
        new_item.skills = item['skills']
        
    

    # on creation of an item object, it receives a uuid
    # if there is no uuid present in the item dict received, then that item is being created for the first time
    # and if there is uuid present, then the item is most likely loaded from the database and should
    # receive its id, and not get a new randomly generated one
    if 'id' in item:
        new_item.id = item['id']
    if 'keep' in item:
        new_item.keep = item['keep']

    return new_item

def save_item(item):
    return item.to_dict()

class Item:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.item_type = ItemType.MISC
        self.name = 'Name of item'
        self.description = 'Description here'
        self.history = {}
        self.tags = []
        self.keep = False
        

    def to_dict(self):
        
        my_dict = {
            'id': self.id,
            'item_type': self.item_type,
            'name': self.name,
            'description': self.description,
            'history': self.history,
            'tags': self.tags,
            'keep': self.keep
        }
        return my_dict

    def identify(self):
        #output = f'{self.name} {self.id} (@cyan{self.item_type}@normal)\n'
        #output = f'{self.name} (@cyan{self.item_type}@normal)\n'
        output = f'{self.name}\n'
        output += f'@cyan{self.description}@normal\n'
        return output

class Consumable(Item):
    def __init__(self):
        super().__init__()
        self.item_type = ItemType.CONSUMABLE
        '''
        self.id = str(uuid.uuid4())
        self.item_type = type(self).__name__.lower()
        self.name = 'Name of item'
        self.description = 'Description here'
        self.history = {}
        self.tags = []
        '''
        self.skills = []
        self.use_perspectives = {
            'you on you':           'You drink the vile liquid',
            'you on other':         'You splash the vile liquid on #OTHER#',
            'user on user':         '#USER# drinks the vile liquid',
            'user on you':          '#USER# splashes the vile liquid on you',
            'user on other':        '#USER# splashes the vile liquid on #OTHER#'
        }
        

    def to_dict(self):
        my_dict = {
            'id': self.id,
            'item_type': self.item_type,
            'name': self.name,
            'description': self.description,
            'history': self.history,
            'tags': self.tags,
            'keep': self.keep,

            'skills': self.skills
            
        }
        return my_dict

    def identify(self):
        output = super().identify()
        
        id_to_name, name_to_id = FACTORY.use_manager.get_skills()
        output += f'Contents: {[id_to_name[skill_id] for skill_id in self.skills]}'
        #output += f'Contents: {self.skills}'
        return output


class Equipment(Item):
    def __init__(self):
        super().__init__()
        self.item_type = ItemType.EQUIPMENT
        '''
        self.id = str(uuid.uuid4())
        self.item_type = type(self).__name__.lower()
        self.name = 'Name of item'
        self.description = 'Description here'
        self.history = {}
        self.tags = []
        '''

        self.slot = EquipmentSlotType.TRINKET
        self.equiped = False
        
        self.stats = {
            StatType.HPMAX: 0,
            StatType.MPMAX: 0,
            StatType.ARMOR: 0,
            StatType.MARMOR:0,
            StatType.BODY: 0,
            StatType.MIND: 0,
            StatType.SOUL: 0

            }

        self.requirements = {
            StatType.HPMAX: 0,
            StatType.MPMAX: 0,
            StatType.ARMOR: 0,
            StatType.MARMOR:0,
            StatType.BODY: 0,
            StatType.MIND: 0,
            StatType.SOUL: 0,
            StatType.LVL: 0
            }

    def to_dict(self):
        my_dict = {
            'id': self.id,
            'item_type': self.item_type,
            'name': self.name,
            'description': self.description,
            'history': self.history,
            'tags': self.tags,
            'keep': self.keep,
            'slot': self.slot,
            'equiped': self.equiped,
            'stats': self.stats,
            'requirements': self.requirements
        }

        return my_dict

    def set_stat(stat, value):
        self.stats[stat] = value

    def identify(self):


        #print('identifying')
        output = super().identify()
        s = self.stats
        r = self.requirements
        if self.slot == None:
            return output
        output += f'Slot: {self.slot} '
        if self.equiped:
            output += f'{"@green(Equiped)@normal"}'
        output += '\n'
        output += f'{StatType.LVL}: {r[StatType.LVL]}\n'
        space = 9
        output += f'@normal{"Stat":<{space}} {"Bonus":<{space}} {"Req":<{space}}\n'
        for stat in self.stats.keys():
            s = self.stats[stat]
            r = self.requirements[stat]
            if r == 0 and s == 0:
                continue
            output += f'@normal{stat:<{space}} {s:<{space}} {r:<{space}}\n'
        '''
        output += f'@normal{"Stat":<{space}} {"Bonus":<{space}} {"Req":<{space}}\n'
        output += f'@normal{"HP":<{space}} {s["hp_max"]:<{space}} {r["hp_max"]:<{space}}\n'
        output += f'@normal{"MP":<{space}} {s["mp_max"]:<{space}} {r["mp_max"]:<{space}}\n'
        #output += f'@cyan{"Damage":<{space}} {s["damage"]:<{space}} {r["damage"]:<{space}}\n'
        output += f'@normal{"Armor":<{space}} {s["armor"]:<{space}} {r["armor"]:<{space}}\n'
        output += f'@normal{"Marmor":<{space}} {s["marmor"]:<{space}} {r["marmor"]:<{space}}\n'
        output += f'@normal{"STR":<{space}} {s["str"]:<{space}} {r["str"]:<{space}}\n'
        output += f'@normal{"DEX":<{space}} {s["dex"]:<{space}} {r["dex"]:<{space}}\n'
        output += f'@normal{"INT":<{space}} {s["int"]:<{space}} {r["int"]:<{space}}\n'
        output += f'@normal{"LUK":<{space}} {s["luk"]:<{space}} {r["luk"]:<{space}}\n'
        '''
        return output





        
        


