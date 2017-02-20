import pickle
import os

from containers import Room
from containers import Container
from containers import Safe

from PlayerObj import PlayerObj

from items import Item
from items import Key
from items import Weapon

from npcs import Guide
from npcs import NonePlayerObj
from npcs import Zombie

from guides import GuideTut

room_dict = {
              'bedroom'       : Room.Room('bedroom'),
              'landing'       : Room.Room('landing'),
              'stairs'        : Room.Room('stairs'),
              'hall'          : Room.Room('hall'),
              'lounge'        : Room.Room('lounge'),
              'kitchen'       : Room.Room('kitchen'),
              'conservatory'  : Room.Room('conservatory'),
              'heaven'        : Room.Room('heaven')
            }

container_dict = {
                  'shelf'         : Container.Container(room_dict['hall'],         'shelf'),
                  'bed'           : Container.Container(room_dict['bedroom'],      'bed'),
                  'table'         : Container.Container(room_dict['kitchen'],      'table'),
                  'cupboards'     : Container.Container(room_dict['kitchen'],      'cupboards'),
                  'body'          : Container.Container(room_dict['kitchen'],      'corpse'),
                  'body_2'        : Container.Container(room_dict['conservatory'], 'corpse'),

                  'safe_kitchen'  : Safe.Safe(room_dict['kitchen'],                'safe', 256342),
                  'safe_bedroom'  : Safe.Safe(room_dict['bedroom'],                'bedroom safe', 'x')
                 }

item_dict = {
             'key_safe_bedroom'  : Key.Key(container_dict['safe_kitchen'], [container_dict['safe_bedroom']]),
             'key_kitchen'       : Key.Key(container_dict['shelf'], [room_dict['kitchen'], room_dict['hall']]),
             'key_conservatory'  : Key.Key(container_dict['table'], [room_dict['conservatory'], room_dict['kitchen']]),

             'knife'             : Weapon.Weapon(room_dict['kitchen'], 'knife', 15),
             'knife_2'           : Weapon.Weapon(container_dict['body'], 'knife', 15),
             'note'              : Item.Item(container_dict['body'], 'note')
            }

container_dict['shelf'].desc         = 'A set of white, wooden shelves.'
container_dict['bed'].desc           = 'A bed with a mutilated mattress. All the springs and most of the stuffing has been stripped away.'
container_dict['table'].desc         = 'An intact 4-legged dining table.'
container_dict['cupboards'].desc     = 'Cupboards surround the room, although most have no doors and have had the hinges removed.'
container_dict['body'].desc          = 'A corpse leaves an acrid scent in the room. Scars cover his body and dried blood covers his neck from a large open wound caused by a knife.'
container_dict['body_2'].desc        = 'A corpse, mostly intact. 2 bullet holes fill his chest and head.'
container_dict['safe_kitchen'].desc  = 'A metal safe with an electric code lock.'
container_dict['safe_bedroom'].desc  = 'A metal safe with a key hole.'

item_dict['key_safe_bedroom'].desc  = 'A small key, like a window key.'
item_dict['key_kitchen'].desc       = 'A large bolt-lock key.'
item_dict['key_conservatory'].desc  = 'A small key but too small to be for an external door.'
item_dict['knife'].desc             = 'A sharp blade covered in blood.'
item_dict['knife_2'].desc           = 'A sharp blade covered in blood.'
item_dict['note'].desc              = 'A crumpled piece of paper with `256342` written on it.'

room_dict['bedroom'].addExit(room_dict['landing'])

room_dict['landing'].addExit(room_dict['stairs'])

room_dict['stairs'].addExit(room_dict['hall'])

room_dict['hall'].addExit(room_dict['kitchen'])
room_dict['hall'].addExit(room_dict['lounge'])

room_dict['lounge'].addExit(room_dict['kitchen'])

room_dict['kitchen'].addExit(room_dict['conservatory'])
room_dict['kitchen'].locked = [room_dict['hall']]

room_dict['conservatory'].locked = [room_dict['kitchen']]

player = PlayerObj(room_dict['lounge'], 100)

guides_dict = {
               'tutorial' : Guide.Guide('Tutorial', player)
              }

npcs_dict = {
             'zombie' : Zombie.Zombie(room_dict['conservatory'],'zombie',80)
            }

NonePlayerObj.NonePlayerObj.global_access_rooms['heaven'] = room_dict['heaven']
npcs_dict['zombie'].dmg = 2

def events():
  guides_dict['tutorial'].tracking = player
  guides_dict['tutorial'].addEventListener(['room'],             [ room_dict['lounge'] ],                                                   GuideTut.room_lounge_tut)
  guides_dict['tutorial'].addEventListener(['room'],             [ room_dict['kitchen'] ],                                                  GuideTut.room_kitchen_tut)
  guides_dict['tutorial'].addEventListener(['room', 'inv'],      [ room_dict['kitchen'] , item_dict['knife']],                              GuideTut.inv_knife_tut)
  guides_dict['tutorial'].addEventListener(['room', 'inv'],      [ room_dict['kitchen'] , item_dict['note']],                               GuideTut.inv_note_tut)
  guides_dict['tutorial'].addEventListener(['room', 'inv'],      [ room_dict['kitchen'] , item_dict['key_conservatory']],                   GuideTut.inv_key_tut)
  guides_dict['tutorial'].addEventListener(['room', 'unlock_r'], [ room_dict['kitchen'] ,[room_dict['kitchen'],room_dict['conservatory']]], GuideTut.unlock_conservatory_tut)
  guides_dict['tutorial'].addEventListener(['room', 'unlock_s'], [ room_dict['kitchen'] ,container_dict['safe_kitchen']],                   GuideTut.unlock_safe_tut)

def resetEvents():
  guides_dict['tutorial'].orderedevents = []

    ## STARTUP ##
events()

print('\n\n\nTo save your game at any point, type in `save` followed by a space and a file name.\nTo load a save, type in `load` and the file name.\nType in `load` with no file name to view all available saves.\n')

def refreshGuides():
  guides_dict['tutorial'].scanEventListener()

def refreshNpcs():
  for i,j in npcs_dict.items():
    j.move()

def refreshPlayer():
  player.refresh()

refreshGuides()

while player.playing == True:
  action = input(' > ')
  if action[:5] == 'save ':
    try:
      os.makedirs('saves/' + action[5:].strip())
    except:
      pass
    f = open('saves/' + action[5:].strip() + '/room_dict','wb')
    pickle.Pickler(f,2).dump(room_dict)
    f.close()
    f = open('saves/' + action[5:].strip() + '/container_dict','wb')
    pickle.Pickler(f,2).dump(container_dict)
    f.close()
    f = open('saves/' + action[5:].strip() + '/item_dict','wb')
    pickle.Pickler(f,2).dump(item_dict)
    f.close()
    f = open('saves/' + action[5:].strip() + '/guides_dict','wb')
    pickle.Pickler(f,2).dump(guides_dict)
    f.close()
    f = open('saves/' + action[5:].strip() + '/npcs_dict','wb')
    pickle.Pickler(f,2).dump(npcs_dict)
    f.close()
    f = open('saves/' + action[5:].strip() + '/player','wb')
    pickle.Pickler(f,2).dump(player)
    f.close()
  elif action[:5] == 'load ':
    resetEvents()
    f = open('saves/' + action[5:].strip() + '/room_dict','rb')
    pickle.load(f)
    f.close()
    f = open('saves/' + action[5:].strip() + '/container_dict','rb')
    container_dict = pickle.load(f)
    f.close()
    f = open('saves/' + action[5:].strip() + '/item_dict','rb')
    item_dict = pickle.load(f)
    f.close()
    f = open('saves/' + action[5:].strip() + '/guides_dict','rb')
    guides_dict = pickle.load(f)
    f.close()
    f = open('saves/' + action[5:].strip() + '/npcs_dict','rb')
    npcs_dict = pickle.load(f)
    f.close()
    f = open('saves/' + action[5:].strip() + '/player','rb')
    player = pickle.load(f)
    f.close()
    events()
  elif action[:4] == 'load':
    print('Available saves:')
    for x in os.listdir('saves/'):
      print(' - ' + str(x))
  else:
    while not player.doAction(action):
      print('Since that was a light action, nothing moved')
      action = input(' > ')

  refreshGuides()
  refreshNpcs()

exit('While loop fell through.')
