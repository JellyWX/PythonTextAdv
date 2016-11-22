import random
from os import listdir

class Room():
  name = ''
  exits = ''
  contents = ''
  locked = False

  def __init__(self, n):
    self.name = n
    self.exits = []
    self.contents = []
    self.locked = False
    print('N:spawned in a room. name:' + self.name + ', exits:' + str(self.exits))

  def eval(self):
    print('N:room has ' + str(self.exits) + ' exits and is called ' + self.name)

  def addExit(self, e):
    self.exits.append(e)

  def addContainer(self, c):
    self.contents.append(c.name)

  def search(self):
    print('N:rooms contents are ' + str(self.contents))

class Container(object):
  room = ''
  name = ''
  contents = ''

  def __init__(self, r, n):
    self.room = r
    self.name = n
    self.contents = []
    print('N:created container ' + self.name + ' with no contents at ' + self.room.name)
    self.room.addContainer(self)

  def addContent(self, c):
    self.contents.append(c.name)

  def removeContent(self, c):
    self.contents.remove(c.name)

  def search(self):
    print('N:containers contents are ' + str(self.contents))

class Item(object):
  name = ''
  carriable = True
  container = ''


  def __init__(self, c, n):
    self.container = c
    self.name = n
    self.carriable = True
    print('N:created a new ' + self.name + ' in ' + self.container.name)
    self.container.addContent(self)

  def collect(self, collector):
    self.container.removeContent(self)
    self.container = collector

class PlayerObj(object):
  health = 0
  room = ''
  inventory = ''

  def __init__(self, r, h):
    self.room = r
    self.health = h
    self.inventory = []
    print('N:new player object spawned in at ' + self.room.name)

  def addItem(self, i):
    self.inventory.append(i.name)
    i.collect(self)

  def doAction(self, action):
    action = action.strip(' ')
    if action == 'rooms':
      self.room.eval()

    elif action.split(' ')[0] == 'room':
      try:
        if eval(action.split(' ')[1]).name in self.room.exits:
          if eval(action.split(' ')[1]).locked == True:
            print('The room is locked')
          else:
            print(self.room.name + ' >> ' + eval(action.split(' ')[1]).name)
            self.room = eval(action.split(' ')[1])

        else:
          print('Room not available for travel. Use `> rooms` to find available rooms.')

      except:
        print('Room name entered not found. USAGE: `> room <name>` (Must be a connected room. Find connected rooms using `> rooms`)')

    elif action.split(' ')[0] == 'collect':
      try:
        if eval(action.split(' ')[1]).name in self.room.contents:
          if eval(action.split(' ')[2]).name in eval(action.split(' ')[1]).contents:
            if eval(action.split(' ')[2]).carriable == True:
              self.addItem(eval(action.split(' ')[2]))
            else:
              print('Item cant be carried')
          else:
            print('Item couldnt be found')
        else:
          print('Couldnt find container')
      except:
        print('Failed to collect said item')

    elif action.split(' ')[0] == 'scan':
      self.room.search()

    elif action.split(' ')[0] == 'search':
      try:
        eval(action.split(' ')[1]).search()
      except:
        print('Container not found')

    elif action.split(' ')[0] == 'inventory':
      print(self.inventory)

    elif action == 'exit':
      exit()

bedroom = Room('bedroom')
landing = Room('landing')
stairs = Room('stairs')
hall = Room('hall')
kitchen = Room('kitchen')

shelf = Container(hall, 'shelf')
key = Item(shelf, 'key')

bedroom.addExit('landing')

landing.addExit('bedroom')
landing.addExit('stairs')

stairs.addExit('landing')
stairs.addExit('hall')

hall.addExit('kitchen')
hall.addExit('stairs')

kitchen.addExit('hall')
kitchen.locked = True

player = PlayerObj(hall, 100)

playing = True

while(playing == True):
  action = input(' > ')
  player.doAction(action)
