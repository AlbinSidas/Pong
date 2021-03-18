# A Pong Game
As a project request during a job application a pong game project was requested.<br>
The requirements where:
* It's a two player game.
* A server should hold the gamestate and by this configuration the players will connect through network to the server to gain the gamestate.
* Languages and stacks are decided by the programmer. 
* The project should take hours and not days to complete. (It doesn't need to be perfect)

## Setup
Run this command in the root directory togehter with package files for node.
```
npm install
```
Next move into the `Client` directory to do:
```
pip3 -r install requirements.txt
``` 
Now all dependencies should be done. <br>
Next is to start the Node server with:<br>
```
node server.js
```
Then it's free to start the clients:
```
python3 Client/main.py
```

If you wish to reset the server status (as it's only handles one game and does not reset state when one player loses)<br>
you may start up a new client and before pressing enter to start the game, press "r" to have a reset server-state board.

## Tech argumentation:
I've choosen a Python3 frontend and a node Express backend to fulfill this task as I've previously created a game in pyGame (although fully local) and have had experience with how pyGame handles inputs and drawing on the local client. Express is used as this is what I have most previous experiance with from work and school, although a better backendserver would probably be a Go-server to have better control over parallelisations, hard-typed instances of objects etc. But as the task is said to take shorter time I've opted for techniques in which i have the most previous experience.  

## Estimated worktime ~13hrs
With inspiration of structure of a previously developed snake game:<br>
https://github.com/AlbinSidas/Snake/tree/master/Snake-v2.0

## Author
Albin Sidås <br>
2021-02 - 2021-03

## Improvments:
* Very "laggy feel" because the refreshrates are not well synced
* Collision to the left is not correct which most likely is 
  because sloppy maths in the bounce function of the ball most often when speed 
  is quite high of ball
* Holding down a key could easily be implemented by including a button down 
  in the lookup table within game_state to check if a key have been let up, 
  if not it request a new up action.
* Would be good with a balance update to take speed of ball divided by some amount 
  to set speed of players.
* A better architecture than the current one would be to have socket connections towards
  the gameserver and let the gameserver announce updates on a set intervall rather
  than syncing requests depending on how often requests are arriving to the server. 

## Feedback on the intervju and things that will not be changed by the author
* The synchronization problems which can occur and manifest in that a player can not move is most likely
  due to the implementation where the server checks how recent the most recent update was, if both clients
  sends updates in that short timespan one of the clients will never get to send it's moves and therefore
  on client does not get to make moves. 
  
* The server does not need to hold a 2d array rather it should just hold the dimensions as the only thing 
that is checked are the boundries within the gameboard world

* The collisionhandling fits better in the gameBoard serverside to let the game handle the collision rather
than letting the ball handle collision towards other entities as this will force the ball to know of other entities. 

* Only sending information with GET requests is not optimal in a security measure.

* It's possible as the implementation holds right now for one client to start spamming updates while the ball 
is on the opposing side of the board  to speed up the updatespeed and also the updates of the ball and make
the ball move faster than the fixed rate. This is a problem which I tried to handle with "timeSinceUpdate" 
yet this did not follow into the latest implementation and will cause problems if there's a malicious player.

* Because of the request based architecture instead of a socket implementation the clients will send requests
even when the player have not made a move and might therefore also overload the server. 

* To more accuretly represent the serverstate of the board the initialization function of the entities could be
used each time instead of creating instances of the entity classes and updating only the positions of these entities. 

* The sizes of the entities should rather be within the entities rather being decided by the gameboard. 

* Probably some more comments were made but those are the ones i remember after ~10hrs. 


### Closing thoughts
It was a very interesting project which gave me a heads up that I've got a lot to learn, especially in being able to handle
more advanced networking between clients and especially within a server - client architecture. I could have used another tech-stack
as using a javascript backend and a python3 frontend may seem a bit backwards to the usual case, and using already existing frameworks
for a full python3 implementation could probably have worked better as python3 is the language I've worked in the longest. 
