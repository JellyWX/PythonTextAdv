import random
from os import listdir

class Room():
  name = ''
  exits = ''
  contents = ''

  def __init__(self, n):
    self.name = n
    self.exits = []
    self.contents = ''
    print('N:spawned in a room. name:' + self.name + ', exits:' + str(self.exits))

  def eval(self):
    print('N:room has ' + str(self.exits) + ' exits and is called ' + self.name)

  def addExit(self, e):
    self.exits.append(e)

class Container(object):
  room = ''
  name = ''
  subcontainers = []

  def __init__(self, r, n):
    self.room = r
    self.name = n
    print('N:created container ' + self.name + 'with no contents at ' + self.room)


class SubContainer(Container):
  name = ''
  contents = []
  container = ''

  def __init__(self, c, n):
    self.name = n
    self.container = c
    print('N:spawned a subcontainer inside container ' + self.container.name)

  def eval(self):
    print('N:subcontainer ' + self.name + ', of ' + self.container + ', contains ' + self.contents)


class PlayerObj(object):
  health = 0
  room = ''
  inventory = []

  def __init__(self, r, h):
    self.room = r
    self.health = h
    print('N:new player object spawned in at ' + self.room.name)

  def doAction(self, action):
    if action == 'rooms':
      self.room.eval()
    elif action.split(' ')[0] == 'room':
      self.room = eval(action.split(' ')[1])
      print(self.room.name)


    elif action == 'exit':
      exit()

bedroom = Room('bedroom')
landing = Room('landing')
stairs = Room('stairs')

bedroom.addExit('landing')
landing.addExit('bedroom')
landing.addExit('stairs')
stairs.addExit('landing')

player = PlayerObj(bedroom, 100)

playing = True

while(playing == True):
  action = input(' > ')
  player.doAction(action)
