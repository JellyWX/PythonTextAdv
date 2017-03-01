import uuid
from containers import Container
from containers import Safe

class Room(Container.Container):
  def __init__(self, n):
    self.id = uuid.uuid4()

    self.name = n
    self.exits = []
    self.contents = []
    self.room = self
    print('N:spawned in a room. name:' + self.name + ', exits:' + str(self.exits))

  def eval(self):
    print('Room ' + self.name + ' leads to:')
    for x in self.exits:
      print(' - ' + x.name(self) + ' ')

  def search(self):
    print('Room contents:')
    for x in self.contents:
      if (type(x) is Safe.Safe) and (not x.locked):
        print(' - ' + x.name + ' (unlocked) ')
      else:
        print(' - ' + x.name + ' ')

class Exit(object):
  def __init__(self,r1,r2,locked):
    self.id = uuid.uuid4()

    r1.exits.append(self)
    r2.exits.append(self)

    self.rooms = (r1,r2)
    self.locked = locked

  def use(self,user,live=False):
    if not self.locked:
      if user.room == self.rooms[0]:
        user.room.contents.remove(user)
        user.room = self.rooms[1]
        user.room.contents.append(user)
      else:
        user.room.contents.remove(user)
        user.room = self.rooms[0]
        user.room.contents.append(user)
      return True
    else:
      if live:
        print('Error:Connection locked. You must find a way to unlock it first.')
      return False

  def name(self,user):
    if user.room == self.rooms[0]:
      return self.rooms[1].name
    else:
      return self.rooms[0].name

  def __eq__(self,com):
    return isinstance(com,type(self)) and com.id == self.id

  def __hash__(self):
    return hash(self.id)
