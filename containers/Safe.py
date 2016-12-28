from containers import Container

class Safe(Container.Container):
  def __init__(self, r, n, p):
    self.room = r
    self.name = n
    self.contents = []
    self.locked = True
    self.corr_pass = p
    self.carriable = False
    print('N:created container ' + self.name + ' with no contents at ' + self.room.name)
    self.room.addContent(self)

  def unlock(self, client):
    if client.room == self.room:
      if self.locked == True:
        for x in client.contents:
          try:
            if x.misc_attr['canUnlock'] == self:
              print('Safe unlocked with key')
              x.name = x.orrname + ' (' + self.name + ')'
              self.locked = False
          except:
            pass
        self.usr_pass = 000000
        if isinstance(self.corr_pass, int):
          while self.locked:
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
        elif self.locked:
          print('You need a key to open this safe')

  def search(self, client):
    if client.room == self.room:
      if self.locked:
        print('Safe is locked')
      else:
        print('Safe contents:')
        for x in self.contents:
          print(' - ' + x.name + ' ')
    else:
      print('Container not available')
