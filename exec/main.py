import pickle
import os

from PlayerObj import PlayerObj
from npcs import NonePlayerObj
from guides import GuideTut

from dictionaries import *

NonePlayerObj.NonePlayerObj.global_access_rooms['heaven'] = room_dict['heaven']
NonePlayerObj.NonePlayerObj.global_access_variables['npcs_dict'] = npcs_dict
NonePlayerObj.NonePlayerObj.global_access_variables['container_dict'] = container_dict

    ## STARTUP ##
events()

print('\n\n\nTo save your game at any point, type in `save` followed by a space and a file name.\nTo load a save, type in `load` and the file name.\nType in `load` with no file name to view all available saves.\n')

def refreshGuides(a):
  guides_dict['tutorial'].scanEventListener(a)

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

refreshGuides(None)

while player.playing == True:
  action = input(' > ')
  while not player.doAction(action):
    print('Since that was a light action, nothing moved')

    refreshGuides(action)

    if action[:5] == 'save ':
      try:
        os.makedirs('saves/' + action[5:].strip())
      except:
        pass
      f = open('saves/' + action[5:].strip() + '/room_dict','wb')
      pickle.Pickler(f,2).dump(room_dict)
      f.close()
      f = open('saves/' + action[5:].strip() + '/exit_dict','wb')
      pickle.Pickler(f,2).dump(exit_dict)
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
      print('Game saved successfully.')
    elif action[:5] == 'load ':
      resetEvents()
      f = open('saves/' + action[5:].strip() + '/room_dict','rb')
      pickle.load(f)
      f.close()
      f = open('saves/' + action[5:].strip() + '/exit_dict','rb')
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
      print('Loaded game successfully.')
    elif action[:4] == 'load':
      print('Available saves:')
      for x in os.listdir('saves/'):
        print(' - ' + str(x))

    action = input(' > ')

  refreshGuides(action)
  refreshNpcs()

exit('While loop fell through.')
