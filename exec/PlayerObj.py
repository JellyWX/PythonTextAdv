import uuid

from random import choice

from containers import Container
from items import Item
from items import Key
from items import Weapon
from npcs import NonePlayerObj

class PlayerObj(Container.Container):
  def __init__(self, r, h):
    self.id = uuid.uuid4()

    self.room = r
    self.room.contents.append(self)
    self.health = h
    self.contents = []
    self.playing = True
    self.weapon = [None, 1]
    self.name = 'player'
    self.pass_bool = False
    self.damage_from = []
    print('N:new player object spawned in at ' + self.room.name)

  def hurt(self, doctor, dmg):
    self.damage_from.append(doctor)
    self.health -= dmg
    print(doctor.name + ' hit you for ' + str(dmg) + ' damage!')

  def unlock(self, a):
    for x in self.room.exits:
      if x.name(self) == a:
        if x.locked:
          for y in self.contents:
            if isinstance(y,Key.Key):
              x.locked = False
              y.name = y.orrname + ' (' + x.name(self) + ')'
              print('Room unlocked.')
              self.pass_bool = True
              break
        else:
          print('Error:Room not locked.')
    else:
      for x in self.room.contents:
        if x.name == a:
          if isinstance(x,Safe.Safe):
            if x.locked:
              for y in self.contents:
                if isinstance(y,Key.Key):
                  x.locked = False
                  y.name = y.orrname + ' (' + x.name + ')'
                  print('Container unlocked.')
                  self.pass_bool = True
                  break

  def examine(self, i):
    done = False
    for x in self.contents:
      if x.name == i:
        print(x.desc)
        break
    else:
      for x in self.room.contents:
        if x.name == i:
          print(x.desc)
          break
      else:
        print('Couldn\'t find object specified in room or inventory.')

  def drop(self, i):
    done = False
    if 'equiped' in i:
      print('You must unequip the item before dropping')
    for y in self.room.contents:
      if y.name in i:
        for x in self.contents:
          if x.name in i:
            x.move(y)
            self.pass_bool = True
            break
        else:
          print('Couldn\'t find item in inventory by name provided. Use `inv` to view inventory.')
        break
    else:
      for x in self.contents:
        if x.name == i:
          x.move(self.room)
          self.pass_bool = True
          break
      else:
        print('Couldn\'t find item/container. Use `inv` and `scan` to view inventory and room contents.')

  def moveRoom(self, a):
    for x in self.room.exits:
      if x.name(self).lower() == a:
        old = self.room
        if x.use(self,True):
          print(old.name + ' >> ' + self.room.name)
        self.pass_bool = True
        break
    else:
      print('Room name not found. Use `> rooms` to find rooms')

  def attack(self, target):
    for i in self.room.contents:
      if isinstance(i,NonePlayerObj.NonePlayerObj) and i.name == target:
        try:
          i.hurt(self,self.weapon[0].dmg*self.weapon[1])
        except:
          i.hurt(self,6*self.weapon[1])
        print('Hurt ' + target + '!')
        self.weapon[1] = 1
        self.pass_bool = True
        break
    else:
      print('NPC not found.')

  def take(self,a):
    for y in self.room.contents:

      if isinstance(y,PlayerObj) or isinstance(y,NonePlayerObj.NonePlayerObj):
        continue #Filters out NPCs to prevent them getting caught up
      try:
        if y.locked:
          continue #Filters locked containers to prevent the user taking an item that is locked away

      except:
        pass
      if (' ' + y.name + ' ') in a: #Finds if the room object is in the user's input
        if isinstance(y,Container.Container):
          for x in y.contents:
            if (' ' + x.name + ' ') in a:
              if x.carriable:
                x.move(self)
                self.weapon[1] = 1
                i = 1
                for z in self.contents:
                  if z != x:
                    if z.name == x.name:
                      while z.name == x.name: #Block of code that automatically names the item with a '(1)' if it has a similar item in the inventory.
                        x.name = x.orrname + ' (' + str(i) + ')'
                        i += 1
                print('Collected item')
                self.pass_bool = True
                break
              else:
                print('Error: Item specified cannot be carried.')
              break
          else:
            print('Error: Item specified could not be found inside container.')
        elif isinstance(y,Item.Item):
          if y.carriable:
            y.move(self)
            self.weapon[1] = 1
            i = 1
            for z in self.contents:
              if z != y:
                if z.name == y.name:
                  while z.name == y.name:
                    y.name = y.orrname + ' (' + str(i) + ')'
                    i += 1
            print('Collected item')
            self.pass_bool = True
            break
          else:
            print('Error: Item specified cannot be carried.')
        else:
          print('Error: Object of type ' + type(y) + ' cannot be carried or searched.')
        break
    else:
      print('Error: Couldn\'t find object specified.')

  def doAction(self, a):
    self.pass_bool = False
    a = a.strip()
    a = a.lower()
    if a.split(' > ')[0] == 'rooms':
      self.room.eval()
      return False

    elif a[:3] == 'go ':
      a = a[2:]
      a = a.strip()
      self.moveRoom(a)

    elif a[:5] == 'take ':
      a = a[5:]
      a = ' ' + a + ' '
      self.take(a)

    elif a[:5] == 'drop ':
      a = a[4:]
      a = a.strip()
      self.drop(a)

    elif a == 'scan':
      self.room.search()

    elif a[:7] == 'search ':
      a = a[6:]
      a = a.strip()
      for x in self.room.contents:
        if isinstance(x,Container.Container):
          if x.name.lower() == a:
            x.search(self)
            self.pass_bool = True
            break
      else:
        print('Error: Couldn\'t find the specified container in the current room.')

    elif a[:7] == 'unlock ':
      a = a[6:]
      a = a.strip()
      self.unlock(a)

    elif a[:5] == 'look ':
      a = a[4:]
      a = a.strip()
      self.examine(a)
      return False

    elif a[:8] == 'examine ':
      a = a[7:]
      a = a.strip()
      self.examine(a)
      return False

    elif a[:6] == 'equip ':
      a = a[5:]
      a = a.strip()
      for i in self.contents:
        if isinstance(i,Weapon.Weapon):
          if i.name == a:
            try:
              self.weapon[0].name = self.weapon[0].name[:len(a)-10]
            except:
              pass
            self.weapon[0] = i
            i.name += ' (equiped)'
            break
      else:
        print('Error: Couldn\'t find a weapon by that name in your inventory.')

    elif a[:7] == 'attack ':
      a = a[6:]
      a = a.strip()
      self.attack(a)

    elif a == 'wait':
      print(choice(['You take a stance and let the world pass','You raise your hands and stance']) + '...') #TODO Add more messages to this choice
      self.weapon[1] += 0.35
      self.pass_bool = True

    elif a in ['inventory', 'inv', 'i']:
      print('Inventory:')
      for x in self.contents:
        print(' - ' + x.name + ' ')

    elif a in ['help', '?']:
      print('Error:No help manual available currently')

    elif a == 'exit':
      self.playing = False
      self.pass_bool = True

    else:
      print('Not recognised command. Try again')

    return self.pass_bool

  def refresh(self):
    if self.health < 1:
      self.die()

  def die(self):
    print('GAMEOVER. You died.')
    print('You can still load from your last save.')
    self.playing = False
