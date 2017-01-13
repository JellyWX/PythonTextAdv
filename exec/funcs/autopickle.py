import pickle

class specialSausage(object):
  def __init__(self, f, m):
    self.root = f
    self.mode = m

  def pickle(self, target):
    for j in target:
      pickle.Pickler(self.root, self.mode).dump(target)
