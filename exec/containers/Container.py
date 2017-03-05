import uuid

class Container(object):
  def __init__(self, r, n, posni=None, c=[],locked=False,desc='No description is available',carry=False):
    self.id = uuid.uuid4()

    self.room = r
    self.name = n
    self.contents = c
    self.locked = locked
    self.desc = desc
    self.carriable = carry
    print('N:created container ' + self.name + ' with no contents at ' + self.room.name)
    self.room.addContent(self)
    self.postinit(posni)

  def postinit(self,n):
    pass

  def addContent(self, c):
    self.contents.append(c)

  def removeContent(self, c):
    self.contents.remove(c)

  def search(self, client):
    print('Container contents:')
    for x in self.contents:
      print(' - ' + x.name + ' ')

  def __eq__(self,com):
    return isinstance(com,type(self)) and com.id == self.id

  def __hash__(self):
    return hash(self.id)
