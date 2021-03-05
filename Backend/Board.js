const Player = require('./Entities/Player');
const Ball = require('./Entities/Ball');

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

      this.initializeBall();

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
        
        // Also moving them in one step to not be within walls
        let startX = this.entities.players.length == 0 ? 1 : this.gameBoard[0].length - 2;
        let startY = Math.floor(this.gameBoard.length / 2);
        
        let player = new Player(startX, startY, id);        
        this.entities.players.push(player);
        
        return true;
    }

    initializeBall(){
        let startY = Math.floor(this.gameBoard.length / 2);
        let startX = Math.floor(this.gameBoard[0].length / 2);
        let ball = new Ball(startX, startY)
        this.entities.balls.push(ball);
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
