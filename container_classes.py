class Container(object):
  def __init__(self, r, n):
    self.room = r
    self.name = n
    self.contents = []
    self.locked = False
    self.desc = 'No description available'
    self.carriable = False
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

class Room(Container):
  movable = False

  def __init__(self, n):
    self.name = n
    self.exits = []
    self.contents = []
    self.chars = []
    self.locked = []
    self.room = self
    print('N:spawned in a room. name:' + self.name + ', exits:' + str(self.exits))

  def eval(self):
    print('Room ' + self.name + ' leads to:')
    for x in self.exits:
      print(' - ' + x.name + ' ')

  def addExit(self, e):
    self.exits.append(e)
    if not(self in e.exits):
      e.addExit(self)

  def search(self):
    print('Room contents:')
    for x in self.contents:
      if (type(x) is Safe) and (not x.locked):
        print(' - ' + x.name + ' (unlocked) ')
      else:
        print(' - ' + x.name + ' ')

class Item(object):
  def __init__(self, c, n):
    self.container = c
    self.name = n
    self.orrname = n
    self.carriable = True
    self.misc_attr = []
    self.desc = 'No description available'
    print('N:created a new ' + self.name + ' in ' + self.container.name)
    self.container.addContent(self)

  def move(self, collector):
    self.container.removeContent(self)
    self.container = collector
    collector.contents.append(self)

class Safe(Container):
  def __init__(self, r, n, p):
    self.room = r
    self.name = n
    self.contents = []
    self.locked = True
    self.corr_pass = p
    self.carriable = False
    print('N:created container ' + self.name + ' with no contents at ' + self.room.name)
    self.room.addContent(self)

  def unlock(self, client):
    if client.room == self.room:
      if self.locked == True:
        for x in client.contents:
          if ('canUnlock ' + self.name) in x.misc_attr:
            print('Safe unlocked with key')
            x.name = x.orrname + ' (' + self.name + ')'
            self.locked = False
        self.usr_pass = 000000
        if isinstance(self.corr_pass, int):
          while self.locked:
            try:
              self.usr_pass = int(input('Enter a 6 digit passcode. Enter `exit` to escape > '))
              if self.usr_pass == self.corr_pass:
                self.locked = False
                print('Safe unlocked')
                break
              else:
                print('Incorrect passcode')
            except:
              break
        elif self.locked:
          print('You need a key to open this safe')

  def search(self, client):
    if client.room == self.room:
      if self.locked:
        print('Safe is locked')
      else:
        print('Safe contents:')
        for x in self.contents:
          print(' - ' + x.name + ' ')
    else:
      print('Container not available')
