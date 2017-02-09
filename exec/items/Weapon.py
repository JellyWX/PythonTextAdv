from items import Item

class Weapon(Item.Item):
  def __init__(self,item,damage):
    self.inherits = [item]
    self.dmg = damage
