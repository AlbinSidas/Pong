const express = require('express');
const app = express();
const port = 3000;
const Board = require('./Backend/Board.js');

let gameBoard = null;

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
    
    
    res.send(gameBoard);
})

app.get('/move', (req, res) => {
    d = new Date();
    currUpdate = d.getTime();
    timeSinceUpdate = currUpdate - lastUpdate;

    if (timeSinceUpdate > 50){
        lastUpdate = currUpdate;
    } else {
        // If requests are more frequent, just return boardstate.
        res.send(gameBoard);
        return
    }

    let action = req.query.action;
    let identification = req.query.id;

    //gameBoard.collisionCheck();
    
    gameBoard.entities.balls.forEach(ball => {
        ball.update(timeSinceUpdate, gameBoard.entities.players);
    })

    if (action == "Not pressed"){
        res.send(gameBoard);
    } else {
        let player = gameBoard.entities.players.filter(player => player.id == identification)[0];
        player.update(timeSinceUpdate, action);

        res.send(gameBoard);
    }
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})