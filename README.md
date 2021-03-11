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
  because sloppy maths in the bounce function of the ball
