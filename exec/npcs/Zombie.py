import uuid

from random import choice
from npcs import NonePlayerObj
from PlayerObj import PlayerObj
from containers import Container

class Zombie(NonePlayerObj.NonePlayerObj):
  def move(self):
    if self.health < 1 and self.room != self.global_access_rooms['heaven']:
      self.die()
    else:
      for x in self.room.contents:
        if isinstance(x,PlayerObj):
          print(self.name + ': ' + choice(['ARGH','EURGH','HRRGH','ArCK']))
          x.hurt(self,self.dmg)
          break
      else:
        if choice([True,False]): self.moveRoom(choice(self.room.exits))

  def postdeath(self):
    print('The zombie falls swiftly to the ground')
