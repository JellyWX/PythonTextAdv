from containers import Room
from containers import Container
from containers import Safe

from PlayerObj import PlayerObj

from items import Item
from items import Key

from npcs import Guide
from npcs import NonePlayerObj
from npcs import Zombie

bedroom       = Room.Room('bedroom')
landing       = Room.Room('landing')
stairs        = Room.Room('stairs')
hall          = Room.Room('hall')
lounge        = Room.Room('lounge')
kitchen       = Room.Room('kitchen')
conservatory  = Room.Room('conservatory')
heaven        = Room.Room('heaven')

shelf         = Container.Container(hall, 'shelf')
bed           = Container.Container(bedroom, 'bed')
table         = Container.Container(kitchen, 'table')
cupboards     = Container.Container(kitchen, 'cupboards')
body          = Container.Container(kitchen, 'corpse')
body_2        = Container.Container(conservatory, 'corpse')
safe_kitchen  = Safe.Safe(kitchen, 'safe', 256342)
safe_bedroom  = Safe.Safe(bedroom, 'bedroom safe', 'x')

shelf.desc         = 'A set of white, wooden shelves.'
bed.desc           = 'A bed with a mutilated mattress. All the springs and most of the stuffing has been stripped away.'
table.desc         = 'An intact 4-legged dining table.'
cupboards.desc     = 'Cupboards surround the room, although most have no doors and have had the hinges removed.'
body.desc          = 'A corpse leaves an acrid scent in the room. Scars cover his body and dried blood covers his neck from a large open wound caused by a knife.'
body_2.desc        = 'A corpse, mostly intact. 2 bullet holes fill his chest and head.'
safe_kitchen.desc  = 'A metal safe with an electric code lock.'
safe_bedroom.desc  = 'A metal safe with a key hole.'

key_safe_bedroom = Key.Key(safe_kitchen, [safe_bedroom])

key_kitchen = Key.Key(shelf, [kitchen, hall])

key_conservatory = Key.Key(table, [conservatory, kitchen])

knife    = Item.Item(kitchen, 'knife')
knife_2  = Item.Item(body, 'knife')
note     = Item.Item(body, 'note')

key_safe_bedroom.desc  = 'A small key, like a window key.'
key_kitchen.desc       = 'A large bolt-lock key.'
key_conservatory.desc  = 'A small key but too small to be for an external door.'
knife.desc             = 'A sharp blade covered in blood.'
knife_2.desc           = 'A sharp blade covered in blood.'
note.desc              = 'A crumpled piece of paper with `256342` written on it.'

bedroom.addExit(landing)

landing.addExit(stairs)

stairs.addExit(hall)

hall.addExit(kitchen)
hall.addExit(lounge)

lounge.addExit(kitchen)

kitchen.addExit(conservatory)
kitchen.locked = [hall]

conservatory.locked = [kitchen]

player = PlayerObj(lounge, 100)
guide = Guide.Guide('Tutorial', player)

def room_lounge_tut():
  print('Use the command \'rooms\' to see available connections.\nUse the command \'go <room>\' to move rooms. Try to find the kitchen.')
def room_kitchen_tut():
  print('Use the command \'scan\' to view objects in the room.\nUse the command \'take\' to pick up a stray item')
def inv_knife_tut():
  print('Great! You can use the \'inv\' command to view what items you\'re carrying.\nHowever, sometimes an item may be located inside a container. Use \'search <container>\' and \'take <container> <item>\' to collect the note from the corpse')
def inv_note_tut():
  print('Nice! You can use the \'look <item or container>\' command to examine objects. Have a look at some of the things in the room.')

guide.addEventListener(['room'],[lounge],room_lounge_tut)
guide.addEventListener(['room'],[kitchen],room_kitchen_tut)
guide.addEventListener(['room', 'inv'],[kitchen,knife],inv_knife_tut)
guide.addEventListener(['room', 'inv'],[kitchen,note],inv_note_tut)

guide.detection = guide.orderedevents[0][0]
guide.trigger = guide.orderedevents[0][1]
guide.action = guide.orderedevents[0][2]

def refreshGuides():
  guide.scanEventListener()

refreshGuides()

while player.playing == True:
  action = input(' > ')
  player.doAction(action)
  refreshGuides()

exit('While loop fell through.')
