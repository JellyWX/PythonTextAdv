import pickle
import os

from PlayerObj import PlayerObj
from npcs import NonePlayerObj
from guides import GuideTut

from dictionaries import *

NonePlayerObj.NonePlayerObj.global_access_rooms['heaven'] = room_dict['heaven']
NonePlayerObj.NonePlayerObj.global_access_variables['npcs_dict'] = npcs_dict
NonePlayerObj.NonePlayerObj.global_access_variables['container_dict'] = container_dict

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
  npcs_done = False
  while not npcs_done:
    try:
      for i,j in npcs_dict.items():
        j.move()
      npcs_done = True
    except:
      npcs_done = False

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
    print('Game saved.')
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
    print('Loaded game.')
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
