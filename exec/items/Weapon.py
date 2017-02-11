from items import Item

class Weapon(Item.Item):
  def postinit(self, dmg):
    if isinstance(dmg,int):
      self.dmg = dmg
    else:
      exit('Throw: Weapon damage must be an integer.')
