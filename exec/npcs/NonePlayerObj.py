from containers import Container
import uuid

class NonePlayerObj(Container.Container):
  def __init__(self, r, n, h, dmg=0):
    self.id = uuid.uuid4()

    self.room = r
    self.name = n
    self.health = h
    self.attack = dmg
    self.damage_from = []
    self.contents = []
    self.room.contents.append(self)

  def moveRoom(self, r):
    if self.room in r.locked or r in self.room.locked:
      pass
    else:
      self.room.contents.remove(self)
      self.room = r
      self.room.contents.append(self)

  def die(self):
    self.moveRoom(room_dict['heaven'])

  def hurt(self, doctor, dmg):
    self.damage_from.append(doctor)
    self.health -= dmg
