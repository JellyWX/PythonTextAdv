class NonePlayerObj(object):
  def __init__(self, r, n, h):
    self.room = r
    self.name = n
    self.health = h
    self.room.chars.append(self)

  def moveRoom(self, r):
    if self.room in r.locked or r in self.room.locked:
      pass
    else:
      self.room.chars.remove(self)
      self.room = r
      self.room.chars.append(self)

  def die(self):
    self.moveRoom(heaven)
