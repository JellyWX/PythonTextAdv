class Container(object):
  def __init__(self, r, n):
    self.room = r
    self.name = n
    self.contents = []
    self.locked = False
    self.movable = False
    self.desc = 'No description available'
    print('N:created container ' + self.name + ' with no contents at ' + self.room.name)
    self.room.addContent(self)

  def addContent(self, c):
    self.contents.append(c)

  def removeContent(self, c):
    self.contents.remove(c)

  def search(self, client):
    if client.room == self.room:
      print('Container contents:')
      for x in self.contents:
        print(' - ' + x.name + ' ')
    else:
      print('Container not available')

class Room(Container):

  def __init__(self, n):
    self.name = n
    self.exits = []
    self.contents = []
    self.locked = False
    self.room = self
    self.barricade = []
    print('N:spawned in a room. name:' + self.name + ', exits:' + str(self.exits))

  def eval(self):
    print('Room ' + self.name + ' leads to:')
    for x in self.exits:
      print(' - ' + x.name + ' ')

  def addExit(self, e):
    self.exits.append(e)

  def search(self):
    print('Room contents:')
    for x in self.contents:
      print(' - ' + x.name + ' ')

class Item(object):
  def __init__(self, c, n):
    self.container = c
    self.name = n
    self.carriable = True
    self.misc_attr = []
    self.desc = 'No description available'
    print('N:created a new ' + self.name + ' in ' + self.container.name)
    self.container.addContent(self)

  def move(self, collector):
    self.container.removeContent(self)
    self.container = collector
    collector.contents.append(self)

class Safe(Container):
  def __init__(self, r, n, p):
    self.room = r
    self.name = n
    self.contents = []
    self.locked = True
    self.corr_pass = p
    print('N:created container ' + self.name + ' with no contents at ' + self.room.name)
    self.room.addContent(self)

  def unlock(self, client):
    if client.room == self.room:
      if self.locked == True:
        for x in client.contents:
          if 'canUnlock ' + self.name in x.misc_attr:
            print('Safe unlocked with key')
            x.name += ' (' + self.name + ')'
            self.locked = False
        self.usr_pass = 000000
        if isinstance(self.corr_pass, int):
          while(self.locked == True):
            try:
              self.usr_pass = int(input('Enter a 6 digit passcode. Enter `exit` to escape > '))
              if self.usr_pass == self.corr_pass:
                self.locked = False
                print('Safe unlocked')
                break
              else:
                print('Incorrect passcode')
            except:
              break
        elif self.locked == True:
          print('You need a key to open this safe')
  def search(self, client):
    if client.room == self.room:
      if self.locked == True:
        print('Safe is locked')
      else:
        print('Safe contents:')
        for x in self.contents:
          print(' - ' + x.name + ' ')
    else:
      print('Container not available')

class PlayerObj(Container):
  def __init__(self, r, h):
    self.room = r
    self.health = h
    self.contents = []
    print('N:new player object spawned in at ' + self.room.name)

  def unlock(self, r):
    if r.locked == True:
      for i in self.contents:
        if ('canUnlock ' + r.name) in i.misc_attr:
          r.locked = False
          i.name += ' (' + r.name + ')'

  def doAction(self, a):
    a = a.strip(' ')
    if a == 'rooms':
      self.room.eval()

    elif a.split(' ')[0] == 'room':
      for x in self.room.exits:
        if x.name == a.split(' ')[1]:
          if x.locked == True:
            print('The room is locked. Unlock rooms using `> unlock <room>`')
          elif len(x.barricade) > 0:
            print('Room is barricaded. Remove barricades using `> unblock <room>`')
          else:
            print(self.room.name + ' >> ' + a.split(' ')[1])
            self.room = x

    elif a.split(' ')[0] in ['collect', 'take']:
      if len(a.split(' ')) == 3:
        for y in self.room.contents:
          try:
            if y.locked == True:
              continue
          except:
            pass
          if y.name == a.split(' ')[1]:
            for x in y.contents:
              if x.name == a.split(' ')[2]:
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
                else:
                  print('Item cant be carried')
      elif len(a.split(' ')) == 2:
        for x in self.room.contents:
          if x.name == a.split(' ')[1]:
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
            else:
              print('Item cant be carried')
      else:
        print('Failed to evaluate collect')

    elif a.split(' ')[0] == 'drop':
      if len(a.split(' ')) == 3:
        for y in self.room.contents:
          if y.name == a.split(' ')[2]:
            for x in self.contents:
              if x.name == a.split(' ')[1]:
                x.move(y)
      else:
        for x in self.contents:
          if x.name == a.split(' ')[1]:
            x.move(self.room)

    elif a.split(' ')[0] == 'scan':
      self.room.search()

    elif a.split(' ')[0] == 'search':
      try:
        for x in self.room.contents:
          if x.name == a.split(' ')[1]:
            x.search(self)
      except:
        print('Container not found')

    elif a.split(' ')[0] in 'inventory':
      print('contents:')
      for x in self.contents:
        print(' - ' + x.name + ' ')

    elif a.split(' ')[0] == 'unlock':
      done = False
      for x in self.room.exits:
        if x.name == a.split(' ')[1]:
          self.unlock(x)
          done = True
          print('yes')
      if done == False:
        for x in self.room.contents:
          if x.name == a.split(' ')[1]:
            x.unlock(self)

    elif a.split(' ')[0] in ['examine', 'look']:
      done = False
      for x in self.contents:
        if x.name == a.split(' ')[1]:
          print(x.desc)
          done = True
      if done == False:
        for x in self.room.contents:
          if x.name == a.split(' ')[1]:
            print(x.desc)


    elif a == 'exit':
      exit()

    else:
      print('Not recognised command. Try again')

bedroom = Room('bedroom')
landing = Room('landing')
stairs = Room('stairs')
hall = Room('hall')
kitchen = Room('kitchen')
conservatory = Room('conservatory')

shelf = Container(hall, 'shelf')
bed = Container(bedroom, 'bed')
table = Container(kitchen, 'table')
cupboards = Container(kitchen, 'cupboards')
body = Container(kitchen, 'corpse')
body_2 = Container(conservatory, 'corpse')
safe_kitchen = Safe(kitchen, 'safe', 256342)
safe_bedroom = Safe(bedroom, 'safe', 'x')

shelf.desc = 'A set of white, wooden shelves.'
bed.desc = 'A bed with a mutilated mattress. All the springs and most of the stuffing has been stripped away.'
table.desc = 'An intact 4-legged dining table.'
cupboards.desc = 'Cupboards surround the room, although most have no doors and have had the hinges removed.'
body.desc = 'A corpse leaves an acrid scent in the room. Scars cover his body and dried blood covers his neck from a large open wound caused by a knife.'
body_2.desc = 'A corpse, mostly intact. 2 bullet holes fill his chest and head.'
safe_kitchen.desc = 'A metal safe with an electric code lock.'
safe_bedroom.desc = 'A metal safe with a key hole.'

key_safe_bedroom = Item(safe_kitchen, 'key')
key_safe_bedroom.misc_attr.append('canUnlock safe_bedroom')

key_kitchen = Item(shelf, 'key')
key_kitchen.misc_attr.append('canUnlock kitchen')

key_conservatory = Item(table, 'key')
key_conservatory.misc_attr.append('canUnlock conservatory')

knife = Item(kitchen, 'knife')
knife_2 = Item(body, 'knife')

note = Item(body, 'note')

key_safe_bedroom.desc = 'A small key, like a window key.'
key_kitchen.desc = 'A large bolt-lock key.'
key_conservatory.desc = 'A small key but too small to be for an external door.'
knife.desc = 'A sharp blade covered in blood.'
knife_2.desc = 'A sharp blade covered in blood.'
note.desc = 'A crumpled piece of paper with `256342` written on it.'

bedroom.addExit(landing)

landing.addExit(bedroom)
landing.addExit(stairs)

stairs.addExit(landing)
stairs.addExit(hall)

hall.addExit(kitchen)
hall.addExit(stairs)

kitchen.addExit(hall)
kitchen.addExit(conservatory)
kitchen.locked = True

conservatory.addExit(kitchen)
conservatory.locked = True

player = PlayerObj(kitchen, 100)

playing = True

while(playing == True):
  action = input(' > ')
  player.doAction(action)
