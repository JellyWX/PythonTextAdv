from containers import Container
import uuid

class NonePlayerObj(Container.Container):
  global_access_rooms = {}
  global_access_variables = {}
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

  def predeath(self):
    pass
  def postdeath(self):
    pass

  def die(self):
    if self.room != self.global_access_rooms['heaven']:
      self.predeath()
      print(self.name + ' has died to ' + self.damage_from[-1].name)
      self.moveRoom(self.global_access_rooms['heaven'])

      for i,j in self.global_access_variables['npcs_dict'].items():
        if j == self:
          del(self.global_access_variables['npcs_dict'][i])
          break
      self.postdeath()

  def hurt(self, doctor, dmg):
    self.damage_from.append(doctor)
    self.health -= dmg
