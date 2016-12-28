class Container(object):
  def __init__(self, r, n):
    self.room = r
    self.name = n
    self.contents = []
    self.locked = False
    self.desc = 'No description available'
    self.carriable = False
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
