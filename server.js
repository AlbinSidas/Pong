const express = require('express');
const app = express();
const port = 3000;
const Board = require('./Backend/Board.js');

let gameBoard = null;
let key_converter = {
    1073741906 : "up",
    1073741905 : "down",
    1073741904 : "left",
    1073741903 : "right"
};

let d = new Date();
let lastUpdate = d.getTime();
let timeSinceUpdate = (d.getTime() - lastUpdate);

app.get('/initialize', (req, res) => {
    let playerID = req.query.id;
   
    // Success indicates successfully adding a new player.
    let success = true;
    if (gameBoard == null){
        gameBoard = new Board(60,40);
        success = gameBoard.initializePlayer(playerID, enviroment=40);
    } else {
        // There is a active board and therefore also a connected player
        success = gameBoard.initializePlayer(playerID);
        // If there are already 2 players playing an error message will be shown to further players.
    } 

    gameBoard.success = success;
    
    // TODO OBS DENNA FÖR TESTANDE AV FRONTEND
    gameBoard.success = true;
    
    res.send(gameBoard);
})

app.get('/move', (req, res) => {
    /* 
      A player makes a move 
      Check identification of the player too see which player
      is making a move

      Then update the gamestate accordingly.
    */

    /* 
      DETTA KOMMER VARA TICK FUNKTIONEN
      DENNA BÖR ALLTSÅ GE TILLBAKA BOLLENS UPPDATERING

      BOLLEN FÅR RÖRA SIG BASERAT PÅ SEVERNS KLOCKA
      PÅ X TID RÖR DEN SIG DISTANS.

      Samma sak, uppdatera board endast på efter X delay
    */
    d = new Date();
    currUpdate = d.getTime();
    timeSinceUpdate = currUpdate - lastUpdate;

    // Verkar ligga på ungefär 200 på min laptop
    // 0.1s (~10frames per sec)
   if (timeSinceUpdate > 200){
        lastUpdate = currUpdate;
    } else {
        // If requests are more frequent, just return boardstate.
        res.send(gameBoard);
        return
    }

    let action = req.query.action;
    let identification = req.query.id;

    
    // Uppdatera bollposition
    gameBoard.entities.balls.forEach(ball => {
        ball.update(timeSinceUpdate);
    })

    if (action == "Not pressed"){
        res.send(gameBoard);
    } else {
        let player = gameBoard.entities.players.filter(player => player.id == identification)[0];
        player.update(timeSinceUpdate, action);

        res.send(gameBoard);
    }
    // Ta ut rätt player baserat på id

    console.log(gameBoard.entities.balls)
    //res.send('Hello World!');
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})



/* 
Tankar inför backend:

Starta ett game när första spelaren connectar:

1. En första init görs då en spelare startar sin connection, alltså i screen när den startar upp bör detta göras.
2. När denna request kommer ska spelplanen initieras på backend och en spelare ska läggas till
3. I väntan på att en till spelare connectar kommer bollen inte att röra sig
4. När den andra spelaren connectat??? gjort ett anrop att den ansluter så kommer bollen starta efter X tid
5. För att skilja på spelarna kommer de att instancieras och jag kan hålla koll på identification genom clientens genereade ID
6. 


Gör initialize



1. Skapa en funktion som bygger upp start state för en karta
2. När denna karta skickas till klienterna ska klienten kunna rita upp denna
3. När en klient gör en move, skicka denna till servern
4. Servern tar emot move och uppdaterar state # OBS HA NÅGON SORTS SYNCHRONIZERING HÄR FÖR BÄGGE SPELARNA

  - Kanske går att kolla på timestamps för varje move, och uppdatera varje 0.1s eller liknande?

5. Done?


*/