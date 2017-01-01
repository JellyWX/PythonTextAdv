from random import choice
from npcs import NonePlayerObj

class Zombie(NonePlayerObj.NonePlayerObj):
  def __init__(self, r, n, h):
    self.room = r
    self.name = n
    self.health = h

  def move(self):
    for x in self.room.chars:
      if type(x) == PlayerObj:
        pass ##Attack player##
      else:
        moveRoom(choice(self.room.exits))

    if health < 1:
      self.die()
