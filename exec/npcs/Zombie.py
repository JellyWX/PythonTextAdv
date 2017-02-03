from random import choice
from npcs import NonePlayerObj
from PlayerObj import PlayerObj

class Zombie(NonePlayerObj.NonePlayerObj):
  def move(self):
    for x in self.room.chars:
      if type(x) == PlayerObj:
        print('sosig')
        break
    else:
      self.moveRoom(choice(self.room.exits))

    if self.health < 1:
      self.die()
