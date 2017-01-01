#Python Text Adventure Engine
##What is it?
**PythonTextAdv** is an engine for basic text adventure games. It provides a basic class system that can be used to create text adventure games in python. It is simple to use.
###How can I use it?
Download the source from my GitHub (by downloading it from there you can confirm the download is secure and not harmful to your device). Enter the folder and find the file `main.py`. By editing this file, you can create the game. For more information read on.
###How can I run it?
Execute the file `main.py` in its directory. There are 2 scripts provided, `execture.sh` and `execute.bat`. Both of these are for running it on Windows or Linux. If these files don't run, you may need to install python. **You need to use python 3 to run this application.**
###Can I mod it?
**YES**. I would love you to mod it. If you make changes you think are good for efficiency (speed vs. file size) or cool additions/improvements, do add them to a fork of the repository and I will consider implementing them.
###What games are there made in this engine?
The engine comes with a game made by me. I might also load more with it. If I see any cool creations, I will link them here.
##Using the engine
###Getting started
If you haven't already, you need a text editor. For Linux, I recommend either Atom by GitHub or Gedit (also just called 'Text Editor'). On Windows, I recommend Atom or Notepad++. It's also good to have a bit of Python knowledge before attempting this. By the fact that you're here I can presume you already have all of this.
###Rooms
####Making a room
You should be able to pick up a lot of this from the pre-existing code. To make a room, you must refer to the class containers/Room.Room. You can use Room.Room to create a room. A room takes 1 parameter - a name. The name of any object will be what it appear to be to the user of the game. It doesn't have to match the variable name. so, to create a room you can do `room1 = Room.Room('New room')`.
####Linking rooms
To link 2 rooms together, you can append to the exits of a room. The premade `addExit()` method can be used to connect 2 rooms together. So for example `room1.addExit(room2)` presuming you've already made room1 and room2. You don't need to add the exit to room2; this is done automatically.
####Locking rooms
To lock a room, you can alter the 'locked' variable. The 'locked' variable is a list which can be used to note from which direction a room is locked. Say we have rooms 1,2 and 3 set out as below:

____________
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|   room1 = Room.Room('new room')

|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;2&nbsp;&nbsp;|   room2 = Room.Room('new room2')

|&nbsp;1&nbsp;&nbsp;|----&nbsp;|   room3 = Room.Room('new room3')

|&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;3&nbsp;&nbsp;|   room1.addExit(room2)

|&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|   room1.addExit(room3)

|__________|   room3.addExit(room2)

If you wanted to, say, lock room 2, then you can use `room2.locked = [room1, room3]` or `room1.locked = [room2];room3.locked = [room2]` where the ; is a linebreak.
If you only typed `room2.locked = [room1]`, you could still access the room by going first into room3 and then into room2.
####Adding a player
To add a player and test your game, you must create a player object. This can be done in one line using `player = PlayerObj(room1, 100)`. The first parameter is the room in which the player starts, the second is the health of the player. However, if you now try to play the game, you should notice it won't ask you for any input. This is because you need to add a loop to get user input. Add a while loop at the bottom that links to the `player.playing` variable which requests input. When it gets the input, feed it to `player.doAction(input)` to be processed by the player entity.
