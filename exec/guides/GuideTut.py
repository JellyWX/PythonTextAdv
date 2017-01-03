def room_lounge_tut():
  print('Use the command \'rooms\' to see available connections.\nUse the command \'go <room>\' to move rooms. Try to find the kitchen.')

def room_kitchen_tut():
  print('Use the command \'scan\' to view objects in the room.\nUse the command \'take\' to pick up a stray item')

def inv_knife_tut():
  print('Great! You can use the \'inv\' command to view what items you\'re carrying.\nHowever, sometimes an item may be located inside a container. Use \'search <container>\' and \'take <container> <item>\' to collect the note from the corpse')

def inv_note_tut():
  print('Nice! You can use the \'look <item or container>\' command to examine objects. Have a look at some of the things in the room and your inventory. Once you\'ve done that, try and find another key.')

def inv_key_tut():
  print('Now, with the key you\'ve found, unlock a room. Try to move into the conservatory and you\'ll notice it is locked. Use the command `unlock <room>` to unlock the conservatory.')

def unlock_conservatory_tut():
  print('Well done. You can also use the unlock command to unlock safes. Scan the kitchen and using the look and unlock command, unlock the safe.')

def unlock_safe_tut():
  print('Good, you figured it out. Now, using the key from the safe, unlock the `bedroom safe`.')
