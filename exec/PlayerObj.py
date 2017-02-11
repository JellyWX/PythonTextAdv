import uuid
from containers import Container
from items import Key

class PlayerObj(Container.Container):
  def __init__(self, r, h):
    self.id = uuid.uuid4()

    self.room = r
    self.room.contents.append(self)
    self.health = h
    self.contents = []
    self.playing = True
    self.weapon = None
    print('N:new player object spawned in at ' + self.room.name)

  def unlock(self, r):
    if (self.room in r.locked) or (r in self.room.locked):
      for i in self.contents:
        if type(i) == Key.Key:
          if (self.room in i.unlocks) and (r in i.unlocks):
            try:
              r.locked.remove(self.room)
            except:
              self.room.locked.remove(r)
            i.name = i.orrname + ' (' + r.name + ')'
            print('Room unlocked')
    else:
      print('Room not locked')

  def examine(self, i):
    done = False
    for x in self.contents:
      if x.name == i:
        print(x.desc)
        done = True
    if not done:
      for x in self.room.contents:
        if x.name == i:
          print(x.desc)

  def drop(self, i):
    done = False
    for y in self.room.contents:
      if y.name in i:
        for x in self.contents:
          if x.name in i:
            x.move(y)
            done = True
    if not done:
      for x in self.contents:
        if x.name == i:
          x.move(self.room)

  def moveRoom(self, i):
    for x in self.room.exits:
      if x.name.lower() == i:
        if self.room in x.locked:
          print('The connection is locked. Unlock rooms using `> unlock <room>`')
        elif x in self.room.locked:
          print('The connection is locked. Unlock rooms using `> unlock <room>`')
        elif True in x.locked:
          print('The room is locked. Unlock rooms using `> unlock <room>`')
        else:
          print(self.room.name + ' >> ' + i)
          self.room.contents.remove(self)
          self.room = x
          self.room.contents.append(self)
        break
    else:
      print('Room name not found. Use `> rooms` to find rooms')

  def attack(self, target):
    for i in room.contents:
      if isinstance(i,NonePlayerObject):
        i.hurt(self,10)

  def doAction(self, a):
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
      done = False
      for y in self.room.contents:
        try:
          if y.locked:
            continue
        except:
          pass
        if (' ' + y.name + ' ') in a:
          try:
            for x in y.contents:
              if (' ' + x.name + ' ') in a:
                if x.carriable == True:
                  x.move(self)
                  i = 1
                  j = x.name
                  for z in self.contents:
                    if z != x:
                      if z.name == x.name:
                        while z.name == x.name:
                          x.name = j + ' (' + str(i) + ')'
                          i += 1
                  print('Collected item')
                  done = True
                  break
                else:
                  print('Item cant be carried')
          except:
            break
      if not done:
        for x in self.room.contents:
          if (' ' + x.name + ' ') == a:
            if x.carriable:
              x.move(self)
              i = 1
              j = x.name
              for z in self.contents:
                if z != x:
                  if z.name == x.name:
                    while z.name == x.name:
                      x.name = j + ' (' + str(i) + ')'
                      i += 1
              print('Collected item')
              done = True
              break
            else:
              print('Item cant be carried')
        else:
          print('Couldn\'t find item stated.')

    elif a[:5] == 'drop ':
      a = a[4:]
      a = a.strip()
      self.drop(a)

    elif a == 'scan':
      self.room.search()
      return False

    elif a[:7] == 'search ':
      a = a[6:]
      a = a.strip()
      try:
        for x in self.room.contents:
          if x.name.lower() == a:
            x.search(self)
      except:
        print('Container not found')

    elif a[:7] == 'unlock ':
      a = a[6:]
      a = a.strip()
      done = False
      for x in self.room.exits:
        if x.name == a:
          self.unlock(x)
          done = True

      if done == False:
        for x in self.room.contents:
          if x.name == a:
            x.unlock(self)

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

    elif a[:7] == 'attack ':
      a = a[6:]
      a.strip()
      self.attack(a)

    elif a in ['inventory', 'inv', 'i']:
      print('Inventory:')
      for x in self.contents:
        print(' - ' + x.name + ' ')
      return False

    elif a in ['help', '?']:
      print('No help manual available currently')
      return False

    elif a == 'exit':
      self.playing = False

    else:
      print('Not recognised command. Try again')
      return False
    
    return True

  def refresh(self):
    if self.health < 1:
      self.die()

  def die(self):
    print('GAMEOVER. You died.')
    print('You can still load from your last save.')
    self.playing = False
