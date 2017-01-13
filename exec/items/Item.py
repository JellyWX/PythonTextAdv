class Item(object):
  def __init__(self, c, n):
    self.uid = n
    self.container = c
    self.name = n
    self.orrname = n
    self.carriable = True
    self.misc_attr = {}
    self.desc = 'No description available'
    print('N:created a new ' + self.name + ' in ' + self.container.name)
    self.container.addContent(self)

  def move(self, collector):
    self.container.removeContent(self)
    self.container = collector
    collector.contents.append(self)
