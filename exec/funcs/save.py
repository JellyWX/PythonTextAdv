def saveGame(a):
  f = open(a + 'room_dict', 'wb')
  for k, v in room_dict.items():
    f.write(v.contents)
    f.write(v.chars)
    f.write(v.locked)
  f.close()
  f = open(a + 'container_dict', 'wb')
  #for k, v in container_dict.items():
    #f.append
