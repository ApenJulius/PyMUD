import yaml
from enum import Enum, auto
import configuration.map.map_loader
import csv
import os
import configuration.read_from_excel as rfe

SkillScriptValuesToNames = {
    'levels':       'LEVEL',
    'damage':       'DMG-AMP',
    'chance':       'CHANCE',
    'hp_cost':      'HP-COST',
    'mp_cost':      'MP-COST',
    'duration':     'DURATION',
    'cooldown':     'COOLDOWN'
}

class ItemType:
    MISC = 'misc'
    EQUIPMENT = 'equipment'
    CONSUMABLE = 'consumable'
    ERROR = 'error_item'
    name = {
        MISC: 'Misc',
        EQUIPMENT: 'Equipment',
        CONSUMABLE: 'Consumable',
        ERROR: 'Error Item'
    }

class DamageType:
    PHYSICAL = 'physical'
    MAGICAL = 'magical'
    HEALING = 'healing'
    PURE = 'pure'
    CANCELLED = 'cancelled' # Cancels all damage

class ActorStatusType:
    NORMAL = 'Normal'
    FIGHTING = 'Fighting'
    DEAD = 'Dead'

class EquipmentSlotType:
    HEAD =      'head'
    BODY =      'body'
    WEAPON =    'weapon'
    TRINKET =   'trinket'
    RELIC   =   'relic'
    name = {
        HEAD: 'Head',
        BODY: 'Body',
        WEAPON: 'Weapon',
        TRINKET: 'Trinket',
        RELIC:   'Relic'
    }
    '''
    NECK =      'neck'
    CHEST =     'chest'
    HANDS =     'hands'
    BELT =      'belt'
    LEGS =      'legs'
    FEET =      'feet'
    TRINKET =   'trinket'
    PRIMARY =   'primary'
    SECONDARY = 'secondary'
    name = {
        HEAD:      'Head',
        NECK:      'Neck',
        CHEST:     'Chest',
        HANDS:     'Hands',
        BELT:      'Belt',
        LEGS:      'Legs',
        FEET:      'Feet',
        TRINKET:   'Trinket',
        PRIMARY:   'Primary',
        SECONDARY: 'Secondary'
    }
    '''

class StatType:
    HPMAX =     'hp_max'
    MPMAX =     'mp_max'
    HP =        'hp'
    MP =        'mp'
    GRIT =      'grit'
    FLOW =      'flow'
    MIND =      'mind'
    SOUL =      'soul'
    ARMOR =     'armor'
    MARMOR =    'marmor'
    EXP =       'exp'
    LVL =       'lvl'
    PP =        'pp'

    # not saved in db
    THREAT =    'threat'
    
    name = {
        HPMAX:  'Max Health',
        MPMAX:  'Max Magicka',
        HP:     'Health',
        MP:     'Magicka',
        GRIT:   'Grit',
        FLOW:   'Flow',
        MIND:   'Mind',
        SOUL:   'Soul',
        ARMOR:  'Armor',
        MARMOR: 'Marmor',
        EXP:    'Experience',
        LVL:    'Level',
        PP:     'Practice Points',

        # not saved in db
        THREAT: 'Threat'
    }

data = rfe.load()
ITEMS = data['items']
ENEMIES = data['enemies']
SKILLS = data['skills']

WORLD = {}
SPLASH_SCREENS = {}

def load():
    print('reloading')
    data = rfe.load()
    ITEMS = data['items']
    ENEMIES = data['enemies']
    SKILLS = data['skills']

    from configuration.splashscreens.splash import splash_screens
    SPLASH_SCREENS['screens'] = splash_screens

    '''
    #WORLD = {}
    with open("configuration/world.yaml", "r") as file:
        WORLD_UNFILTERED = yaml.safe_load(file)
        for i in WORLD_UNFILTERED:
            if 'template' not in i:
                WORLD[i] = WORLD_UNFILTERED[i]
    '''
    WORLD['world'] = configuration.map.map_loader.load_map()
    #print(WORLD)


    print('reloaded')

           

