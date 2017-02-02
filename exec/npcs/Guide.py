from containers import Safe
from containers import Room

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
    self.progress = 0
    print('N:started a guide')

  def addEventListener(self, l, s, c):
    self.orderedevents.append([l,s,c])

  def scanEventListener(self):
    self.checks = []
    try:
      self.detection = self.orderedevents[self.progress][0]
      self.trigger = self.orderedevents[self.progress][1]
      self.action = self.orderedevents[self.progress][2]
    except:
      self.detection = [None]
      print(self.name + ' completed')
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
    if 'unlock_s' in self.detection:
      for x in self.trigger:
        if type(x) == Safe.Safe:
          if x.locked == False:
            for y in range(0,len(self.checks)):
              if self.checks[y] == False:
                self.checks[y] = True
                break
    if 'unlock_r' in self.detection:
      for x in self.trigger:
        if type(x) == list:
          if type(x[0]) == Room.Room:
            if (x[0] not in x[1].locked) and (x[1] not in x[0].locked):
              for y in range(0,len(self.checks)):
                if self.checks[y] == False:
                  self.checks[y] = True
                  break
    if False in self.checks:
      pass
    elif True in self.checks:
      self.action()
      self.progress += 1
