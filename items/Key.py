from items import Item

class Key(Item.Item):
  carriable = True
  def __init__(self, c, u):
    self.unlocks = u
    self.container = c
    self.name = 'key'
    self.orrname = self.name
    self.desc = 'A metal key'
    print('N:created a new ' + self.name + ' in ' + self.container.name)
    self.container.addContent(self)
