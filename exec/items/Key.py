from items import Item

class Key(Item.Item):
  def postinit(self, u):
    self.unlocks = u
    self.desc = 'A metal key'
