class NonePlayerObj(object):
  def __init__(self, r, n, h):
    self.room = r
    self.name = n
    self.health = h

  def moveRoom(self, r):
    self.room.chars.remove(self)
    self.room = r
    self.room.chars.append(self)

  def die(self):
    self.moveRoom(heaven)
