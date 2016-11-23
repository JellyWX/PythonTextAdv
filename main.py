class Room():
  name = ''
  exits = ''
  contents = ''
  locked = False
  room = ''

  def __init__(self, n):
    self.name = n
    self.exits = []
    self.contents = []
    self.locked = False
    self.room = self
    print('N:spawned in a room. name:' + self.name + ', exits:' + str(self.exits))

  def eval(self):
    print('Room ' + self.name + ' leads to:')
    for x in self.exits:
      print(' - ' + x.name + ' ')

  def addExit(self, e):
    self.exits.append(e)

  def addContent(self, c):
    self.contents.append(c)

  def removeContent(self, c):
    self.contents.remove(c)

  def search(self):
    print('Room contents:')
    for x in self.contents:
      print(' - ' + x.name + ' ')

class Container(object):
  room = ''
  name = ''
  contents = ''

  def __init__(self, r, n):
    self.room = r
    self.name = n
    self.contents = []
    print('N:created container ' + self.name + ' with no contents at ' + self.room.name)
    self.room.addContent(self)

  def addContent(self, c):
    self.contents.append(c)

  def removeContent(self, c):
    self.contents.remove(c)

  def search(self, client):
    if client.room == self.room:
      print('Container contents:')
      for x in self.contents:
        print(' - ' + x.name + ' ')
    else:
      print('Container not available')

class Item(object):
  name = ''
  carriable = True
  container = ''
  misc_attr = ''

  def __init__(self, c, n):
    self.container = c
    self.name = n
    self.carriable = True
    self.misc_attr = []
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
    self.inventory.append(i)
    i.collect(self)

  def unlock(self, r):
    if r.locked == True:
      for i in self.inventory:
        if ('canUnlock ' + r.name) in i.misc_attr:
          r.locked = False
          i.name += ' (' + r.name + ')'

  def doAction(self, a):
    a = a.strip(' ')
    if a == 'rooms':
      self.room.eval()

    elif a.split(' ')[0] == 'room':
      try:
        if eval(a.split(' ')[1]) in self.room.exits:
          if eval(a.split(' ')[1]).locked == True:
            print('The room is locked')
          else:
            print(self.room.name + ' >> ' + a.split(' ')[1])
            self.room = eval(a.split(' ')[1])

        else:
          print('Room not available for travel. Use `> rooms` to find available rooms.')

      except:
        print('Room name entered not found. USAGE: `> room <name>` (Must be a connected room. Find connected rooms using `> rooms`)')

    elif a.split(' ')[0] == 'collect':
      try:
        if eval(a.split(' ')[1]).room == self.room:
          for x in eval(a.split(' ')[1]).contents:
            if x.name == a.split(' ')[2]:
              if x.carriable == True:
                self.addItem(x)
                print('Collected item')
              else:
                print('Item cant be carried')
        else:
          print('Container cant be found')
      except:
        print('Couldnt find item specified')
    elif a.split(' ')[0] == 'scan':
      self.room.search()

    elif a.split(' ')[0] == 'search':
      try:
        eval(a.split(' ')[1]).search(self)
      except:
        print('Container not found')

    elif a.split(' ')[0] == 'inventory':
      print('Inventory:')
      for x in self.inventory:
        print(' - ' + x.name + ' ')

    elif a.split(' ')[0] == 'unlock':
      self.unlock(eval(a.split(' ')[1]))

    elif a == 'exit':
      exit()

bedroom = Room('bedroom')
landing = Room('landing')
stairs = Room('stairs')
hall = Room('hall')
kitchen = Room('kitchen')
conservatory = Room('conservatory')

shelf = Container(hall, 'shelf')
bed = Container(bedroom, 'bed')
table = Container(kitchen, 'table')
cupboards = Container(kitchen, 'cupboards')

key_kitchen = Item(shelf, 'key')
key_kitchen.misc_attr.append('canUnlock kitchen')

key_conservatory = Item(table, 'key')
key_conservatory.misc_attr.append('canUnlock conservatory')

knife = Item(kitchen, 'knife')

bedroom.addExit(landing)

landing.addExit(bedroom)
landing.addExit(stairs)

stairs.addExit(landing)
stairs.addExit(hall)

hall.addExit(kitchen)
hall.addExit(stairs)

kitchen.addExit(hall)
kitchen.addExit(conservatory)
kitchen.locked = True

conservatory.addExit(kitchen)
conservatory.locked = True

player = PlayerObj(bedroom, 100)

playing = True

while(playing == True):
  action = input(' > ')
  player.doAction(action)
