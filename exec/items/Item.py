import uuid

class Item(object):
  def __init__(self, c, n, posni=None):
    self.id = uuid.uuid4()

    self.container = c
    self.name = n
    self.orrname = n
    self.carriable = True
    self.desc = 'No description available'
    print('N:created a new ' + self.name + ' in ' + self.container.name)
    self.container.addContent(self)
    self.postinit(posni)

  def postinit(self, n):
    pass

  def move(self, collector):
    self.container.removeContent(self)
    self.container = collector
    collector.contents.append(self)

  def __eq__(self,com):
    return isinstance(com,type(self)) and com.id == self.id

  def __hash__(self):
    return hash(self.id)
