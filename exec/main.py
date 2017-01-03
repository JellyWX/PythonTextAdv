from containers import Room
from containers import Container
from containers import Safe

from PlayerObj import PlayerObj

from items import Item
from items import Key

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
              
             'knife'             : Item.Item(room_dict['kitchen'], 'knife'),
             'knife_2'           : Item.Item(container_dict['body'], 'knife'),
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
guide = Guide.Guide('Tutorial', player)

guide.addEventListener(['room'],             [ room_dict['lounge'] ],                                                   GuideTut.room_lounge_tut)
guide.addEventListener(['room'],             [ room_dict['kitchen'] ],                                                  GuideTut.room_kitchen_tut)
guide.addEventListener(['room', 'inv'],      [ room_dict['kitchen'] , item_dict['knife']],                              GuideTut.inv_knife_tut)
guide.addEventListener(['room', 'inv'],      [ room_dict['kitchen'] , item_dict['note']],                               GuideTut.inv_note_tut)
guide.addEventListener(['room', 'inv'],      [ room_dict['kitchen'] , item_dict['key_conservatory']],                   GuideTut.inv_key_tut)
guide.addEventListener(['room', 'unlock_r'], [ room_dict['kitchen'] ,[room_dict['kitchen'],room_dict['conservatory']]], GuideTut.unlock_conservatory_tut)
guide.addEventListener(['room', 'unlock_s'], [ room_dict['kitchen'] ,container_dict['safe_kitchen']],                   GuideTut.unlock_safe_tut)


    ## STARTUP ##

guide.detection = guide.orderedevents[0][0]
guide.trigger = guide.orderedevents[0][1]
guide.action = guide.orderedevents[0][2]

print('\n\n\nTo save your game at any point, type in `save` followed by a space and a file name.\nTo load a save, type in `load` and the file name.\nType in `load` with no file name to view all available saves.\n')

def refreshGuides():
  guide.scanEventListener()

refreshGuides()

while player.playing == True:
  action = input(' > ')
  player.doAction(action)
  refreshGuides()

exit('While loop fell through.')
