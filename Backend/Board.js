const Player = require('./Entities/Player');
//import Player from './Backend/Entities/Player';
//var Paddle = require('./paddle')

class Board {
    constructor(x, y) {
      // Use these to check boundries
      this.boardWidth = x;
      this.boardHeight = y;
      this.tileSize = 10;

      // Entities
      this.gameBoard = this.initializeGameboard();
      
      // entities
      this.entities = {
          'players' :[],
          'balls'   :[]
      }
    }
   
    initializeGameboard() {
        // Initialize based on incoming parameters
        let gameBoard = new Array(this.boardHeight).fill(0)
        for (var row in gameBoard) {
            gameBoard[row] = new Array(this.boardWidth).fill(0)
        }
        
        return gameBoard;
    }

    initializePlayer(id){
        // If there is no connected players, first is connecting
        // and is assigned the furthest left, else to the furthest right.
        if (this.entities.players.length == 2){
            return false;
        }

        let startX = this.entities.players.length == 0 ? 0 : this.gameBoard[0].length - 1;
        let startY = Math.floor(this.gameBoard.length / 2);
        
        let player = new Player(startX, startY, id);
        
        this.entities.players.push(player);
        return true;
    }

    collisionCheck(){

    }
  
    updateTick(){
        console.log("TICK")
        // Make the call to the clients
        fetch()
    }
  }

  module.exports = Board
