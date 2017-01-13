from os import listdir

def main():
  print('Available saves:')
  for x in listdir('saves/'):
    print(' - ' + str(x))
