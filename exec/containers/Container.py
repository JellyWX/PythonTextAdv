import uuid

class Container(object):
  def __init__(self, r, n):
    self.id = uuid.uuid4()

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

  def __eq__(self,com):
    return isinstance(com,type(self)) and com.id == self.id

  def __hash__(self):
    return hash(self.id)
