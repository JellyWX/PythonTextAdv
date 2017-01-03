from containers import Container
from containers import Safe

class Room(Container.Container):
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
      if (type(x) is Safe.Safe) and (not x.locked):
        print(' - ' + x.name + ' (unlocked) ')
      else:
        print(' - ' + x.name + ' ')
