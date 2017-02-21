from random import choice
from npcs import NonePlayerObj
from PlayerObj import PlayerObj
from containers import Container

class Zombie(NonePlayerObj.NonePlayerObj):
  def move(self):
    if self.health < 1:
      self.die()
    else:
      for x in self.room.contents:
        if type(x) == PlayerObj:
          print(self.name + ': ' + choice(['ARGH','EURGH','HRRGH','ArCK']))
          break
      else:
        if choice([True,False]): self.moveRoom(choice(self.room.exits))

  def predeath(self):
    self.deposit = Container.Container(self.room,self.name + ' (dead)')

  def postdeath(self):
    print('The zombie falls quickly to the ground')
