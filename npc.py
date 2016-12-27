from container_classes import *

class Guide(object):
  ## The guide is designed to lead the player through the game and create a storyline ##

  def __init__(self, n, p):
    self.checks = [False]
    self.tracking = p
    self.orderedevents = []
    self.detection = []
    self.trigger = []
    self.action = None
    self.name = n
    print('N:started a guide')

  def addEventListener(self, l, s, c):
    self.orderedevents.append([l,s,c])

  def scanEventListener(self):
    self.checks = []
    for x in self.detection:
      self.checks.append(False)

    if 'inv' in self.detection:
      for i in self.tracking.contents:
        if i in self.trigger:
          y = 0
          for y in range(0,len(self.checks)):
            if self.checks[y] == False:
              self.checks[y] = True
              break
    if 'room' in self.detection:
      if self.tracking.room in self.trigger:
        for y in range(0,len(self.checks)):
          if self.checks[y] == False:
            self.checks[y] = True
            break
    if False in self.checks:
      pass
    elif True in self.checks:
      self.action()
      self.orderedevents.pop(0)
      try:
        self.detection = self.orderedevents[0][0]
        self.trigger = self.orderedevents[0][1]
        self.action = self.orderedevents[0][2]
      except:
        self.detection = [None]
        print(self.name + ' quests completed!')

class NonePlayerObj(object):
  def __init__(self, r, n, h):
    self.room = r
    self.name = n
    self.health = h

  def moveRoom(self, r):
    self.room.chars.remove(self)
    self.room = r
    self.room.chars.append(self)

class Zombie(NonePlayerObj):
  def __init__(self, r, n, h):
    self.room = r
    self.name = n
    self.health = h

  def move(self):
    for x in self.room.chars:
      if type(x) == PlayerObj:
        pass ##Attack player##
      else:
        moveRoom(choice(self.room.exits))

    if health < 1:
      self.die()

  def die(self):
    self.moveRoom(heaven)
