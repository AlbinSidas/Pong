# A Pong Game
As a project request during a job application a pong game project was requested.<br>
The requirements where:
* It's a two player game.
* A server should hold the gamestate and by this configuration the players will connect through network to the server to gain the gamestate.
* Languages and stacks are decided by the programmer. 
* The project should take hours and not days to complete. (It doesn't need to be perfect)

## Tech argumentation:
I've choosen a Python3 frontend and a node Express backend to fulfill this task as I've previously created a game in pyGame (although fully local) and have had experience with how pyGame handles inputs and drawing on the local client. Express is used as this is what I have most previous experiance with from work and school, although a better backendserver would probably be a Go-server to have better control over parallelisations, hard-typed instances of objects etc. But as the task is said to take shorter time I've opted for techniques in which i have the most previous experience.  

## Author
Albin Sidås <br>
2021-02 - 2021-03

# TODO
Tankar inför backend:

1. Skapa en funktion som bygger upp start state för en karta [CHECK]
2. När denna karta skickas till klienterna ska klienten kunna rita upp denna [CHECK]
3. När en klient gör en move, skicka denna till servern
4. Servern tar emot move och uppdaterar state # OBS HA NÅGON SORTS SYNCHRONIZERING HÄR FÖR BÄGGE SPELARNA

  - Kanske går att kolla på timestamps för varje move, och uppdatera varje 0.1s eller liknande?

5. Hantera att rita ut spelare korrekt å den sida de är på just nu
6. Hantera kollisioner för bollen (studsa i väggar och mot spelare)


Gör globala sökningar på TODO och OBS för att finna saker att arbeta vidare på.