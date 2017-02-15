from random import choice
from npcs import NonePlayerObj
from PlayerObj import PlayerObj

class Zombie(NonePlayerObj.NonePlayerObj):
  def move(self):
    for x in self.room.contents:
      if type(x) == PlayerObj:
        print(self.name + ': ' + choice(['ARGH','EURGH','HRRGH','ArCK']))
        break
    else:
      if choice([True,False]): self.moveRoom(choice(self.room.exits))

    if self.health < 1:
      self.die()
